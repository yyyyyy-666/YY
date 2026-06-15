def _extract_val(raw):
    if isinstance(raw, dict):
        return raw.get("min") or raw.get("score") or 0
    return raw or 0

def build_score_timeline(scores):
    raw = {}
    for k, v in scores.items():
        raw[k] = _extract_val(v)

    known = {}
    for yr in ("2023", "2024", "2025"):
        if yr in raw and raw[yr] not in (0, 130):
            known[yr] = raw[yr]

    out = {}
    for year in ("2023", "2024", "2025"):
        in_raw = year in raw
        val = raw.get(year, 0)
        is_placeholder = val in (0, 130)

        if in_raw and not is_placeholder:
            out[year] = {"score": val, "quality": "official"}
        else:
            if year == "2023":
                base = known.get("2024", 0)
                if not base:
                    base = known.get("2025", 0)
                if base:
                    predicted = max(base - 8, 200)
                else:
                    predicted = 450
                out[year] = {"score": predicted, "quality": "estimated"}
            elif year == "2024":
                base = known.get("2023", known.get("2025", 0))
                if base:
                    predicted = min(base + 5, 750)
                else:
                    predicted = 450
                out[year] = {"score": min(predicted, 750), "quality": "estimated"}
            else:
                if "2024" in known and "2023" in known:
                    trend = known["2024"] - known["2023"]
                    predicted = known["2024"] + trend
                elif "2024" in known:
                    predicted = known["2024"]
                elif "2023" in known:
                    predicted = known["2023"]
                else:
                    predicted = 450
                out[year] = {"score": min(predicted, 750), "quality": "predicted"}

    return out

def format_score_timeline(scores):
    timeline = build_score_timeline(scores)
    parts = []
    labels = {"official": "官方", "estimated": "估算", "predicted": "预测"}
    for year in ("2023", "2024", "2025"):
        if year in timeline:
            d = timeline[year]
            label = labels.get(d["quality"], d["quality"])
            parts.append(f"{year}{label}{d['score']}分")
    return " / ".join(parts)

def quality_statistics(all_schools):
    counts = {"official": 0, "estimated": 0, "predicted": 0}
    for name, school in all_schools.items():
        scores = school.get("scores", {})
        if not scores:
            continue
        timeline = build_score_timeline(scores)
        for year_data in timeline.values():
            q = year_data["quality"]
            counts[q] = counts.get(q, 0) + 1
    return counts
