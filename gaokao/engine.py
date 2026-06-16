from .models import (
    StudentInput, AnalysisResult, FamilyCondition,
    CityRecommendation, UniversityRecommendation, MajorRecommendation,
)
from .data.universities import BATCH_LINES
from .data.admissions import get_all_schools, get_latest_official_score, format_timeline_str, normalize_school
from .data.majors import MAJORS, get_dangerous_majors, get_majors_for_school


class ZhangXuefengEngine:

    def analyze(self, student: StudentInput) -> AnalysisResult:
        strategy = self._family_filter(student.family)
        cities = self._city_filter(student)
        universities = self._school_filter(student)
        majors = self._major_filter(student, strategy)
        warnings = self._generate_warnings(majors, student.family)
        summary = self._generate_summary(student, cities, universities, majors)
        return AnalysisResult(
            cities=cities, universities=universities,
            majors=majors, warnings=warnings, summary=summary,
        )

    def _family_filter(self, family: FamilyCondition) -> str:
        if family == FamilyCondition.RICH:
            return "追求热爱"
        elif family == FamilyCondition.NORMAL:
            return "就业导向"
        return "确定性优先"

    def _city_filter(self, student: StudentInput) -> list[CityRecommendation]:
        if student.city_preference:
            return [CityRecommendation(city=student.city_preference, reason="你有明确的城市偏好")]
        tier1 = ["北京", "上海", "广州", "深圳"]
        tier2 = ["杭州", "南京", "成都", "武汉", "西安", "长沙", "南昌"]
        cities = [CityRecommendation(city=c, reason="一线城市，就业机会多") for c in tier1[:2]]
        if student.rank > 10000:
            cities += [CityRecommendation(city=c, reason="新一线城市，性价比高") for c in tier2[:2]]
        return cities

    def _school_filter(self, student: StudentInput) -> list[UniversityRecommendation]:
        score = student.score
        all_schools = get_all_schools()
        matched = []
        for name, u in sorted(all_schools.items(), key=lambda x: get_latest_official_score(x[1]), reverse=True):
            latest = get_latest_official_score(u)
            if latest == 0:
                continue
            diff = score - latest
            if 0 <= diff <= 20:
                tier = "冲"
            elif 20 < diff <= 50:
                tier = "稳"
            elif diff > 50:
                tier = "保"
            else:
                continue
            timeline = normalize_school(u)
            score_str = format_timeline_str(timeline) or f"{latest}分"
            level = u.get("level", "")
            city = u.get("city", "")
            typ = u.get("type", "")
            nature = u.get("nature", "")
            strong = u.get("strong_majors", [])
            strong_str = "、".join(strong[:3]) if strong else ""
            reason = f'{level}，{city}，{typ}，{nature}'
            if strong_str:
                reason += f'，强势专业：{strong_str}'
            matched.append(UniversityRecommendation(
                name=name, tier=tier,
                reason=reason,
                score_range=score_str,
            ))
        if not matched:
            for name, u in sorted(all_schools.items(), key=lambda x: get_latest_official_score(x[1])):
                latest = get_latest_official_score(u)
                if latest > 0 and latest <= score:
                    matched.append(UniversityRecommendation(
                        name=name, tier="保",
                        reason=f'{u.get("level","")}，{u.get("city","")}',
                        score_range=f"{latest}分",
                    ))
                    if len(matched) >= 5:
                        break
        return matched[:12]

    def _major_filter(self, student: StudentInput, strategy: str) -> list[MajorRecommendation]:
        is_vocational = student.score < BATCH_LINES["二本线"]
        pool = get_majors_for_school("综合类", is_vocational)
        if strategy == "确定性优先":
            pool = [m for m in pool if m["employment_rate"] >= 0.9 and "天坑" not in (m.get("warning") or "")]
        elif strategy == "就业导向":
            pool = [m for m in pool if m["employment_rate"] >= 0.85]
        pool.sort(key=lambda m: m["salary_median"], reverse=True)
        return [
            MajorRecommendation(
                name=m["name"], employment_rate=m["employment_rate"],
                salary_median=m["salary_median"],
                reason=f'就业率{m["employment_rate"]*100:.0f}%，薪资{m["salary_median"]}元/月',
                warning=m.get("warning", ""),
                jobs=m.get("jobs", ""),
                industries=m.get("industries", ""),
            )
            for m in pool[:5]
        ]

    def _generate_warnings(self, majors, family):
        warnings = []
        dangerous = get_dangerous_majors()
        if dangerous:
            names = "、".join(m["name"] for m in dangerous[:4])
            warnings.append(f"生化环材四天王（{names}），没读博士别逞强")
        if family == FamilyCondition.POOR:
            warnings.append("家庭条件困难，优先选就业确定性高的专业")
        return warnings

    def _generate_summary(self, student, cities, universities, majors):
        rush = [u for u in universities if u.tier == "冲"]
        stable = [u for u in universities if u.tier == "稳"]
        safe = [u for u in universities if u.tier == "保"]
        parts = []
        if rush: parts.append(f"冲{rush[0].name}")
        if stable: parts.append(f"稳{stable[0].name}")
        if safe: parts.append(f"保{safe[0].name}")
        if cities: parts.append(f"优先去{cities[0].city}")
        if majors: parts.append(f"选{majors[0].name}")
        if student.family == FamilyCondition.POOR:
            parts.append("家里条件一般，就业第一")
        elif student.family == FamilyCondition.RICH:
            parts.append("家里有底，可以选自己喜欢的")
        if student.score >= BATCH_LINES["一本线"]:
            batch = "你过了一本线，"
        elif student.score >= BATCH_LINES["二本线"]:
            batch = "你在二本线以上，"
        else:
            batch = "分数不高，"
        return batch + "，".join(parts) + "。"
