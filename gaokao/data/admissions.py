from gaokao.data.universities import JIANGXI_DATA
from gaokao.data.universities_ext import get_extra_universities

YEARS = ("2023", "2024", "2025")
PLACEHOLDER_VALUES = (0, 130)


def _extract_score(raw):
    if isinstance(raw, dict):
        val = raw.get("min") or raw.get("score") or 0
        section = raw.get("section") or 0
        return val, section
    return raw or 0, 0


def _is_placeholder(val):
    return val in PLACEHOLDER_VALUES


def _quality(val, year, has_real_data):
    if _is_placeholder(val):
        return "estimated"
    if not has_real_data:
        return "missing"
    if year == "2025":
        return "official"
    return "official"


def normalize_school(school):
    name = school.get("name", "")
    scores = school.get("scores", {})
    out = {}
    for yr in YEARS:
        raw = scores.get(yr)
        if raw is None:
            out[yr] = {"score": 0, "section": 0, "quality": "missing"}
        else:
            val, section = _extract_score(raw)
            if _is_placeholder(val):
                base = _get_adjacent_real_score(scores, yr)
                est = max(base - 8, 200) if base else 0
                out[yr] = {"score": est, "section": 0, "quality": "estimated"}
            else:
                out[yr] = {"score": val, "section": section, "quality": "official"}
    return out


def _get_adjacent_real_score(scores, target_year):
    for yr in YEARS:
        if yr == target_year:
            continue
        raw = scores.get(yr)
        if raw is None:
            continue
        val, _ = _extract_score(raw)
        if val not in PLACEHOLDER_VALUES:
            return val
    return 0


def get_all_schools():
    merged = {}
    for school in JIANGXI_DATA:
        name = school.get("name", "")
        if not name:
            continue
        merged[name] = {
            "name": name,
            "level": school.get("level", ""),
            "city": school.get("city", ""),
            "type": school.get("type", ""),
            "nature": school.get("nature", ""),
            "scores": school.get("scores", {}),
            "strong_majors": school.get("strong_majors", []),
            "source": "JIANGXI_DATA",
        }
    for school in get_extra_universities():
        name = school.get("name", "")
        if not name or name in merged:
            continue
        merged[name] = {
            "name": name,
            "level": school.get("level", ""),
            "city": school.get("city", ""),
            "type": school.get("type", ""),
            "nature": school.get("nature", "未知"),
            "scores": school.get("scores", {}),
            "strong_majors": school.get("strong_majors", []),
            "source": "EXT",
        }
    return merged


def get_school_timeline(school):
    return normalize_school(school)


def get_latest_official_score(school):
    timeline = normalize_school(school)
    for yr in reversed(YEARS):
        if timeline[yr]["quality"] == "official":
            return timeline[yr]["score"]
    for yr in reversed(YEARS):
        if timeline[yr]["quality"] == "estimated":
            return timeline[yr]["score"]
    return 0


def get_score_quality_label(timeline, year):
    entry = timeline.get(year, {})
    quality = entry.get("quality", "missing")
    score = entry.get("score", 0)
    if quality == "missing":
        return f"{year}缺失"
    labels = {"official": "官方", "estimated": "估算", "missing": "缺失"}
    label = labels.get(quality, quality)
    return f"{year}{label}{score}分"


def format_timeline_str(timeline):
    parts = []
    for yr in YEARS:
        entry = timeline.get(yr, {})
        if entry.get("quality") == "missing":
            continue
        label = get_score_quality_label(timeline, yr)
        parts.append(label)
    return " / ".join(parts) if parts else ""


def coverage_statistics():
    all_schools = get_all_schools()
    stats = {
        "total": len(all_schools),
        "by_year": {yr: {"official": 0, "estimated": 0, "missing": 0} for yr in YEARS},
    }
    for school in all_schools.values():
        timeline = normalize_school(school)
        for yr in YEARS:
            q = timeline[yr]["quality"]
            stats["by_year"][yr][q] += 1
    return stats
