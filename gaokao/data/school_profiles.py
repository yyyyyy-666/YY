from gaokao.data.school_living import get_school_living
from gaokao.data.rankings_ext import get_ranking_ext
from gaokao.data.financial_aid import SCHOLARSHIP_TYPES, FINANCIAL_PLANNING
from gaokao.data.admissions import get_all_schools, get_school_timeline, format_timeline_str


def get_school_profile(school_name):
    all_schools = get_all_schools()
    school = all_schools.get(school_name)
    if not school:
        return None

    living = get_school_living(school_name) or {}
    ranking = get_ranking_ext(school_name) or {}
    timeline = get_school_timeline(school)
    timeline_str = format_timeline_str(timeline)

    profile = {
        "name": school_name,
        "level": school.get("level", ""),
        "city": school.get("city", ""),
        "type": school.get("type", ""),
        "nature": school.get("nature", ""),
        "strong_majors": school.get("strong_majors", []),
        "source": school.get("source", ""),
        "timeline": timeline,
        "timeline_str": timeline_str,
        "ranking": ranking.get("软科排名", ""),
        "dorm": living.get("宿舍条件", ""),
        "food": living.get("食堂", ""),
        "campus": living.get("校园环境", ""),
        "scholarship": _get_school_scholarship(school_name),
        "risk_notes": _get_risk_notes(school),
    }
    return profile


def _get_school_scholarship(school_name):
    notes = []
    for name, info in SCHOLARSHIP_TYPES.items():
        notes.append(f"{name}: {info.get('金额', '')}")
    return notes


def _get_risk_notes(school):
    notes = []
    nature = school.get("nature", "")
    level = school.get("level", "")
    if "民办" in nature:
        notes.append("民办院校，学费较高")
    if "独立学院" in level:
        notes.append("独立学院，毕业证与本部不同")
    if "中外合作" in str(school.get("type", "")):
        notes.append("中外合作办学，学费高")
    return notes


def format_profile_card(profile):
    if not profile:
        return "未找到该学校"

    parts = []
    parts.append(f"**{profile['name']}**")
    parts.append(f"层次: {profile['level']} | 类型: {profile['type']} | 性质: {profile['nature']}")
    parts.append(f"城市: {profile['city']}")
    if profile["timeline_str"]:
        parts.append(f"录取分数: {profile['timeline_str']}")
    if profile["ranking"]:
        parts.append(f"软科排名: {profile['ranking']}")
    if profile["dorm"]:
        parts.append(f"宿舍: {profile['dorm']}")
    if profile["food"]:
        parts.append(f"食堂: {profile['food']}")
    if profile["strong_majors"]:
        parts.append(f"强势专业: {'、'.join(profile['strong_majors'][:5])}")
    if profile["risk_notes"]:
        parts.append(f"注意: {'; '.join(profile['risk_notes'])}")
    return "\n".join(parts)
