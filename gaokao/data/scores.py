from .universities import JIANGXI_DATA


def get_universities_by_rank(rank: int, province: str = "", subject: str = "") -> dict:
    rush = []
    stable = []
    safe = []

    for u in sorted(JIANGXI_DATA, key=lambda x: x["min_score"], reverse=True):
        diff = u["min_rank"] - rank

        if diff > 0 and diff <= rank * 0.3:
            rush.append(u["name"])
        elif abs(diff) <= rank * 0.15:
            stable.append(u["name"])
        elif diff < 0 and abs(diff) <= rank * 0.5:
            safe.append(u["name"])

    return {"rush": rush[:3], "stable": stable[:3], "safe": safe[:3]}


def get_universities_by_score(score: int, tolerance: int = 15) -> list:
    return [u for u in JIANGXI_DATA if abs(u["min_score"] - score) <= tolerance]
