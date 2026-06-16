from gaokao.data.majors import MAJORS
from gaokao.data.major_details_ext import get_major_deep_analysis_ext
from gaokao.data.employment_deep_ext import get_major_employment_deep_ext
from gaokao.data.major_city_ext import get_major_city_match_ext
from gaokao.data.career_path import get_career_path
from gaokao.data.decision_ext import get_major_score_card_ext


def get_major_profile(major_name):
    base = _find_major(major_name)
    if not base:
        return None

    deep = get_major_deep_analysis_ext(major_name) or {}
    employment = get_major_employment_deep_ext(major_name) or {}
    city_match = get_major_city_match_ext(major_name) or {}
    career = get_career_path(major_name) or {}
    score_card = get_major_score_card_ext(major_name) or {}

    profile = {
        "name": major_name,
        "employment_rate": base.get("employment_rate", 0),
        "salary_median": base.get("salary_median", 0),
        "jobs": base.get("jobs", ""),
        "warning": base.get("warning", ""),
        "salary_growth": deep.get("薪资成长", {}),
        "promotion_path": deep.get("晋升路径", ""),
        "work_intensity": deep.get("工作强度", ""),
        "crisis_35": deep.get("35岁危机", ""),
        "employment_985": employment.get("就业率_985", 0),
        "employment_211": employment.get("就业率_211", 0),
        "employment_normal": employment.get("就业率_双非", 0),
        "salary_985": employment.get("薪资_985", 0),
        "salary_211": employment.get("薪资_211", 0),
        "salary_normal": employment.get("薪资_双非", 0),
        "top_companies": employment.get("头部公司", []),
        "best_cities": _extract_best_cities(city_match),
        "career_path": career.get("典型路径", {}),
        "score_card": score_card,
        "postgraduate_value": score_card.get("考研收益", 0),
        "civil_service_value": _estimate_civil_service(major_name),
        "family_fit": _estimate_family_fit(base, score_card),
    }
    return profile


def _find_major(name):
    for m in MAJORS:
        if m["name"] == name:
            return m
    return None


def _extract_best_cities(city_match):
    if not city_match:
        return []
    cities = []
    for tier, items in city_match.items():
        for c in items:
            cities.append({"city": c.get("city", ""), "tier": tier, "salary": c.get("avg_salary", 0)})
    return sorted(cities, key=lambda x: x.get("salary", 0), reverse=True)[:10]


def _estimate_civil_service(major_name):
    kw = major_name
    if any(k in kw for k in ["法学", "行政", "公共管理", "政治", "社会工作", "汉语言", "新闻"]):
        return 90
    if any(k in kw for k in ["会计", "金融", "计算机", "电子信息", "电气", "土木"]):
        return 70
    if any(k in kw for k in ["医学", "护理", "药学"]):
        return 60
    if any(k in kw for k in ["艺术", "设计", "体育", "音乐"]):
        return 30
    return 50


def _estimate_family_fit(base, score_card):
    salary = base.get("salary_median", 0)
    total = score_card.get("总分", 50)
    if salary >= 8000 and total >= 70:
        return "富裕家庭: 就业前景好，家庭资源可放大优势"
    if salary >= 5000 and total >= 50:
        return "普通家庭: 性价比高，就业确定性强"
    if salary < 4000 or total < 40:
        return "困难家庭: 谨慎选择，优先考虑就业确定性"
    return "普通家庭: 可根据兴趣选择"


def format_major_profile_card(profile):
    if not profile:
        return "未找到该专业"

    parts = []
    parts.append(f"**{profile['name']}**")
    emp_rate = profile['employment_rate']
    if isinstance(emp_rate, (int, float)):
        parts.append(f"就业率: {emp_rate*100:.0f}% | 薪资: {profile['salary_median']}元/月")
    else:
        parts.append(f"就业率: {emp_rate} | 薪资: {profile['salary_median']}元/月")
    if profile["jobs"]:
        parts.append(f"就业方向: {profile['jobs']}")
    if profile["warning"]:
        parts.append(f"注意: {profile['warning']}")
    if profile["promotion_path"]:
        parts.append(f"晋升路径: {profile['promotion_path']}")
    if profile["work_intensity"]:
        parts.append(f"工作强度: {profile['work_intensity']} | 35岁危机: {profile['crisis_35']}")
    if profile["salary_growth"]:
        growth = " → ".join(f"{k}{v}元" for k, v in profile["salary_growth"].items())
        parts.append(f"薪资成长: {growth}")
    if profile["top_companies"]:
        parts.append(f"头部公司: {'、'.join(profile['top_companies'][:5])}")
    if profile["best_cities"]:
        city_names = [c["city"] for c in profile["best_cities"][:5]]
        parts.append(f"最佳就业城市: {'、'.join(city_names)}")
    parts.append(f"考研价值: {profile['postgraduate_value']}/100 | 考公价值: {profile['civil_service_value']}/100")
    parts.append(f"家庭适配: {profile['family_fit']}")
    return "\n".join(parts)
