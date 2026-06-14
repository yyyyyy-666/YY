from .models import AnalysisResult
from .data.cities import get_city_info
from .data.trends import get_industry_trend, SPECIAL_ADMISSION
from .data.zhangxuefeng import ZHANG_XUEFENG_FRAMEWORK, ZHANG_XUEFENG_MAJOR_CATEGORIES, get_major_category
from .data.major_details import get_major_deep_analysis
from .data.school_major_match import get_school_major_match
from .data.advanced import get_province_policy, get_employment_quality, get_career_switch
from .data.postgraduate import get_postgraduate_advice, get_major_curriculum
from .data.employment_deep import get_major_employment_deep
from .data.major_city import get_major_city_match
from .data.decision import get_major_score_card
from .data.rankings import get_school_features
from .data.quickref import get_major_avoid_list, get_major_golden_rules
from .data.province_major import get_province_major_strength
from .data.scenarios import get_major_faq
from .data.tiers import get_school_tier_analysis, get_major_tier_analysis
from .data.combos import get_major_traps, get_major_formulas
from .data.provinces import get_province_batch_lines, get_province_competition
from .data.province_3d import get_province_city_major_3d, get_province_school_recommend
from .data.province_3d_all import get_province_city_major_3d_all
from .data.province_schools_all import get_province_school_recommend_all


def _analyze_trend(score_range: str) -> str:
    import re
    years = re.findall(r'(\d{4})年(\d+)分', score_range)
    if len(years) < 2:
        return ""
    scores = [(int(y), int(s)) for y, s in years]
    scores.sort()
    if len(scores) == 2:
        diff = scores[1][1] - scores[0][1]
        if diff > 5:
            return f"分数线上涨{diff}分（{scores[0][0]}年{scores[0][1]}分 → {scores[1][0]}年{scores[1][1]}分），竞争加剧"
        elif diff < -5:
            return f"分数线下降{abs(diff)}分（{scores[0][0]}年{scores[0][1]}分 → {scores[1][0]}年{scores[1][1]}分），竞争缓和"
        else:
            return f"分数线基本稳定（{scores[0][0]}年{scores[0][1]}分 → {scores[1][0]}年{scores[1][1]}分）"
    elif len(scores) == 3:
        diff_12 = scores[1][1] - scores[0][1]
        diff_23 = scores[2][1] - scores[1][1]
        if diff_23 > 5 and diff_12 > 0:
            return f"连续上涨（{scores[0][0]}年{scores[0][1]}分 → {scores[2][0]}年{scores[2][1]}分），竞争逐年加剧"
        elif diff_23 < -5 and diff_12 < 0:
            return f"连续下降（{scores[0][0]}年{scores[0][1]}分 → {scores[2][0]}年{scores[2][1]}分），竞争逐年缓和"
        elif diff_23 > 5:
            return f"近一年上涨{diff_23}分（{scores[1][0]}年{scores[1][1]}分 → {scores[2][0]}年{scores[2][1]}分），竞争加剧"
        elif diff_23 < -5:
            return f"近一年下降{abs(diff_23)}分（{scores[1][0]}年{scores[1][1]}分 → {scores[2][0]}年{scores[2][1]}分），竞争缓和"
        else:
            return f"三年基本稳定（{scores[0][0]}年{scores[0][1]}分 → {scores[2][0]}年{scores[2][1]}分）"
    return ""


def format_result(result: AnalysisResult) -> str:
    lines = []

    lines.append("=" * 50)
    lines.append("  高考志愿分析报告（张雪峰框架）")
    lines.append("=" * 50)
    lines.append("")

    # 张雪峰五层筛选框架
    lines.append("【张雪峰五层筛选框架】")
    for layer_name, layer_info in ZHANG_XUEFENG_FRAMEWORK.items():
        lines.append(f"  {layer_name}：{layer_info['description']}")
    lines.append("")

    lines.append(f"【总结】{result.summary}")
    lines.append("")

    if result.cities:
        lines.append("【城市推荐】")
        for c in result.cities:
            city_info = get_city_info(c.city)
            salary = city_info.get("avg_salary", 0)
            cost = city_info.get("cost_level", "")
            job = city_info.get("job_market", "")
            highlights = "、".join(city_info.get("highlights", [])[:3])
            lines.append(
                f"  -> {c.city}：{c.reason} | "
                f"平均薪资{salary}元/月，生活成本{cost}，就业市场{job}，优势产业：{highlights}"
            )
        lines.append("")

    if result.universities:
        lines.append("【学校推荐】")
        for tier in ["冲", "稳", "保"]:
            tier_schools = [u for u in result.universities if u.tier == tier]
            if tier_schools:
                lines.append(f"  {tier}：")
                for u in tier_schools:
                    lines.append(f"    -> {u.name}（{u.score_range}）{u.reason}")
                    # 学校特色
                    features = get_school_features(u.name)
                    if features:
                        strongest = features.get("最强专业", [])[:3]
                        if strongest:
                            lines.append(f"        最强专业：{'、'.join(strongest)}")
        lines.append("")
        # 学校层次分析
        if result.universities:
            first_school = result.universities[0]
            if "985" in first_school.reason:
                tier_info = get_school_tier_analysis("985院校")
            elif "211" in first_school.reason:
                tier_info = get_school_tier_analysis("211院校")
            elif "双一流" in first_school.reason:
                tier_info = get_school_tier_analysis("双一流院校")
            else:
                tier_info = get_school_tier_analysis("普通本科")
            if tier_info:
                lines.append("【学校层次分析】")
                lines.append(f"  特征：{tier_info.get('特征', '')}")
                lines.append(f"  薪资水平：{tier_info.get('薪资水平', '')}")
                lines.append(f"  考研率：{tier_info.get('考研率', '')}")
                lines.append(f"  适合人群：{tier_info.get('适合人群', '')}")
                lines.append("")
        lines.append("【录取趋势分析】")
        for u in result.universities[:5]:
            trend = _analyze_trend(u.score_range)
            if trend:
                lines.append(f"  -> {u.name}：{trend}")
        lines.append("")

    if result.majors:
        lines.append("【专业推荐（张雪峰分类）】")
        for m in result.majors:
            warning = f" !! {m.warning}" if m.warning else ""
            jobs = f" | 岗位：{m.jobs}" if m.jobs else ""
            industries = f" | 行业：{m.industries}" if m.industries else ""
            category = get_major_category(m.name)
            lines.append(
                f"  -> {m.name}：就业率 {m.employment_rate*100:.0f}%，"
                f"薪资中位数 {m.salary_median} 元{warning}{jobs}{industries}"
                f" | 分类：{category}"
            )
            # 深度分析
            deep = get_major_deep_analysis(m.name)
            if deep:
                salary = deep.get("薪资成长", {})
                if salary:
                    lines.append(f"      薪资成长：应届{salary.get('应届',0)}元 → 3年{salary.get('3年',0)}元 → 5年{salary.get('5年',0)}元 → 10年{salary.get('10年',0)}元")
                lines.append(f"      晋升路径：{deep.get('晋升路径', '')}")
                lines.append(f"      工作强度：{deep.get('工作强度', '')} | 35岁危机：{deep.get('35岁危机', '')}")
                lines.append(f"      行业周期：{deep.get('行业周期', '')}")
            # 院校-专业匹配
            match = get_school_major_match(m.name)
            if match:
                first = match.get("第一梯队", [])[:4]
                second = match.get("第二梯队", [])[:4]
                if first:
                    lines.append(f"      推荐院校（第一梯队）：{'、'.join(first)}")
                if second:
                    lines.append(f"      推荐院校（第二梯队）：{'、'.join(second)}")
            # 考研/留学建议
            postgrad = get_postgraduate_advice(m.name)
            if postgrad:
                lines.append(f"      考研必要性：{postgrad.get('考研必要性', '')} | 考研难度：{postgrad.get('考研难度', '')}")
                lines.append(f"      考研收益：{postgrad.get('考研收益', '')}")
                if postgrad.get("留学建议"):
                    lines.append(f"      留学建议：{postgrad['留学建议']}")
            # 课程体系
            curriculum = get_major_curriculum(m.name)
            if curriculum:
                core = curriculum.get("核心技能", [])
                langs = curriculum.get("推荐语言", [])
                if core:
                    lines.append(f"      核心技能：{'、'.join(core)}")
                if langs:
                    lines.append(f"      推荐语言：{'、'.join(langs)}")
            # 就业深度分析
            emp_deep = get_major_employment_deep(m.name)
            if emp_deep:
                lines.append(f"      985就业率：{emp_deep.get('就业率_985',0)*100:.0f}% | 211就业率：{emp_deep.get('就业率_211',0)*100:.0f}% | 双非就业率：{emp_deep.get('就业率_双非',0)*100:.0f}%")
                lines.append(f"      985薪资：{emp_deep.get('薪资_985',0)}元/月 | 211薪资：{emp_deep.get('薪资_211',0)}元/月 | 双非薪资：{emp_deep.get('薪资_双非',0)}元/月")
                top_companies = emp_deep.get("头部公司", [])[:4]
                if top_companies:
                    lines.append(f"      头部公司：{'、'.join(top_companies)}")
            # 专业-城市匹配
            city_match = get_major_city_match(m.name)
            if city_match:
                first_cities = city_match.get("第一梯队城市", [])[:3]
                if first_cities:
                    city_str = "、".join([f"{c['city']}({c['avg_salary']}元/月)" for c in first_cities])
                    lines.append(f"      最佳就业城市：{city_str}")
            # 专业评分卡
            score_card = get_major_score_card(m.name)
            if score_card:
                lines.append(f"      综合评分：{score_card.get('总分',0)}/100 | 等级：{score_card.get('等级','')}")
        lines.append("")

    if result.warnings:
        lines.append("【避坑提示】")
        for w in result.warnings:
            lines.append(f"  !! {w}")
        # 补充专业避坑清单
        avoid_list = get_major_avoid_list()
        for category, items in avoid_list.items():
            for item in items[:2]:
                if item["name"] in [m.name for m in result.majors]:
                    lines.append(f"  !! {item['name']}：{item['reason']}，建议替代：{item['alternative']}")
        lines.append("")

    # 张雪峰黄金法则
    lines.append("【张雪峰专业选择黄金法则】")
    rules = get_major_golden_rules()
    for rule_name, rule_info in list(rules.items())[:4]:
        lines.append(f"  {rule_name}：{rule_info['内容']}")
    lines.append("")

    # 常见问题
    faq = get_major_faq()
    if faq:
        lines.append("【常见问题速答】")
        for q, a in list(faq.items())[:5]:
            lines.append(f"  {q}")
            lines.append(f"    {a['A']}")
        lines.append("")

    # 常见陷阱
    traps = get_major_traps()
    if traps:
        lines.append("【常见陷阱提醒】")
        for trap_name, trap_info in list(traps.items())[:3]:
            lines.append(f"  {trap_name}：{trap_info['错误']}")
            lines.append(f"    真相：{trap_info['真相']}")
        lines.append("")

    # 核心公式
    formulas = get_major_formulas()
    if formulas:
        lines.append("【张雪峰核心公式】")
        for formula_name, formula_info in list(formulas.items())[:3]:
            lines.append(f"  {formula_name}：{formula_info['公式']}")
        lines.append("")

    if result.majors:
        industries = set()
        for m in result.majors:
            if m.industries:
                for ind in m.industries.split("、"):
                    industries.add(ind.strip())
        if industries:
            lines.append("【行业趋势参考】")
            for ind in list(industries)[:5]:
                trend = get_industry_trend(ind)
                if trend.get("trend") != "未知":
                    lines.append(
                        f"  -> {ind}：{trend['trend']}，增长率{trend['growth']}，"
                        f"平均薪资{trend['avg_salary']}元/月，{trend['outlook']}"
                    )
            lines.append("")

    lines.append("【特殊招生通道】")
    lines.append("  如果你的分数不够理想，还可以考虑以下通道：")
    for name, info in list(SPECIAL_ADMISSION.items())[:4]:
        lines.append(f"  -> {name}：{info['description']}")
    lines.append("")

    # 省份录取政策
    province_info = get_province_policy("江西省")
    if province_info:
        lines.append("【江西省录取政策】")
        lines.append(f"  高考模式：{province_info.get('高考模式', '')}")
        lines.append(f"  录取规则：{province_info.get('录取规则', '')}")
        lines.append(f"  志愿数量：{province_info.get('志愿数量', '')}")
        if province_info.get("注意事项"):
            for note in province_info["注意事项"]:
                lines.append(f"  注意：{note}")
        lines.append("")

    # 省份批次线
    batch_lines = get_province_batch_lines("江西")
    if batch_lines:
        lines.append("【江西省近年批次线】")
        for year, lines_data in batch_lines.items():
            parts = [f"{k}={v}" for k, v in lines_data.items()]
            lines.append(f"  {year}年：{'，'.join(parts)}")
        lines.append("")

    # 省份竞争度
    competition = get_province_competition("江西")
    if competition:
        lines.append("【江西省竞争度分析】")
        lines.append(f"  考生数：约{competition.get('考生数', 0)}万")
        lines.append(f"  竞争度：{competition.get('竞争度', '')}")
        lines.append(f"  特点：{competition.get('特点', '')}")
        lines.append("")

    # 省份-专业匹配
    province_strength = get_province_major_strength("江西")
    if province_strength:
        lines.append("【江西省专业优势】")
        lines.append(f"  最强专业：{'、'.join(province_strength.get('最强专业', []))}")
        lines.append(f"  最强院校：{'、'.join(province_strength.get('最强院校', []))}")
        lines.append(f"  就业优势：{province_strength.get('就业优势', '')}")
        lines.append(f"  适合人群：{province_strength.get('适合人群', '')}")
        lines.append("")

    # 省份-城市-专业三维匹配
    province_3d = get_province_city_major_3d("江西")
    if not province_3d:
        province_3d = get_province_city_major_3d_all("江西")
    if province_3d:
        lines.append("【江西省最优就业路径】")
        for path in province_3d.get("最优路径", [])[:4]:
            lines.append(f"  -> {path['城市']}+{path['专业']}：{path['理由']}，薪资约{path['薪资']}元/月")
        if province_3d.get("回流建议"):
            lines.append(f"  回流建议：{province_3d['回流建议']}")
        lines.append("")

    # 省份院校推荐
    school_recommend = get_province_school_recommend("江西")
    if not school_recommend:
        school_recommend = get_province_school_recommend_all("江西")
    if school_recommend:
        lines.append("【江西省院校推荐】")
        for level, schools in school_recommend.items():
            lines.append(f"  {level}：{'、'.join(schools)}")
        lines.append("")

    # 就业质量参考
    if result.majors:
        industries = set()
        for m in result.majors:
            if m.industries:
                for ind in m.industries.split("、"):
                    industries.add(ind.strip())
        if industries:
            lines.append("【就业质量参考】")
            for ind in list(industries)[:3]:
                emp = get_employment_quality(ind)
                if emp and emp.get("校招薪资"):
                    salary = emp["校招薪资"]
                    lines.append(
                        f"  -> {ind}：本科{salary.get('本科','')}，硕士{salary.get('硕士','')}，"
                        f"工作强度{emp.get('工作强度','')}，35岁危机{emp.get('35岁危机','')}"
                    )
            lines.append("")

    lines.append("=" * 50)
    return "\n".join(lines)
