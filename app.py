import streamlit as st
import pandas as pd
from gaokao.engine import ZhangXuefengEngine
from gaokao.models import StudentInput, FamilyCondition, SubjectType
from gaokao.data.majors import MAJORS
from gaokao.data.universities import JIANGXI_DATA
from gaokao.data.zhangxuefeng import ZHANG_XUEFENG_FRAMEWORK, ZHANG_XUEFENG_MAJOR_CATEGORIES
from gaokao.data.personality import HOLLAND_CODES, MBTI_MAJOR_MAP, calculate_holland, recommend_majors_by_holland, PERSONALITY_QUESTIONS
from gaokao.data.universities_ext import get_extra_universities
from gaokao.data.major_details_ext import get_major_deep_analysis_ext
from gaokao.data.employment_deep_ext import get_major_employment_deep_ext
from gaokao.data.major_city_ext import get_major_city_match_ext
from gaokao.data.decision_ext import get_major_score_card_ext, get_common_mistakes_ext
from gaokao.data.school_major_match_ext import get_school_major_match_ext
from gaokao.data.rankings_ext import get_ranking_ext
from gaokao.data.school_living import get_school_living, FRESHMAN_TIPS
from gaokao.data.career_path import get_career_path
from gaokao.data.financial_aid import SCHOLARSHIP_TYPES, FINANCIAL_PLANNING
from gaokao.data.quickref import get_major_golden_rules
from gaokao.data.score_quality import format_score_timeline, quality_statistics
from gaokao.data.admissions import get_all_schools as get_merged_schools, format_timeline_str, normalize_school, coverage_statistics

st.set_page_config(page_title="高考志愿策略师", page_icon="\U0001f393", layout="wide")

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');

* { font-family: 'Noto Sans SC', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #f0f4ff 0%, #e8edf5 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-right: none;
}

[data-testid="stSidebar"] .stTitle, 
[data-testid="stSidebar"] .stMarkdown {
    color: white !important;
}

[data-testid="stSidebar"] .stRadio > div {
    gap: 4px;
}

[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.08);
    color: rgba(255,255,255,0.8);
    padding: 12px 16px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.3s ease;
    font-weight: 400;
    cursor: pointer;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.15);
    color: white;
    border-color: rgba(255,255,255,0.2);
    transform: translateX(4px);
}

[data-testid="stSidebar"] .stRadio label[data-selected="true"] {
    background: linear-gradient(135deg, #e8b840 0%, #f5a623 100%) !important;
    color: #1a1a2e !important;
    border-color: #f5a623 !important;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(245, 166, 35, 0.3);
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:first-child {
    margin-top: 8px;
}

h1, h2, h3 {
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

.stButton > button {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: white !important;
    border: none;
    padding: 12px 32px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(26, 26, 46, 0.2);
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(26, 26, 46, 0.3);
    background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
}

.stButton > button:active {
    transform: translateY(0);
}

div[data-testid="stExpander"] {
    background: white;
    border-radius: 14px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    margin-bottom: 12px;
    overflow: hidden;
}

div[data-testid="stExpander"] > div:first-child {
    background: white;
    border-radius: 14px;
    padding: 4px 16px;
}

div[data-testid="stExpander"] > div:first-child:hover {
    background: #f8f9fc;
}

[data-testid="stTab"] {
    background: white;
    border-radius: 12px 12px 0 0;
    padding: 8px 24px;
    font-weight: 500;
}

[data-testid="stTab"][aria-selected="true"] {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: white !important;
}

[data-testid="stDataFrame"] {
    background: white;
    border-radius: 14px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    overflow: hidden;
}

[data-testid="stDataFrame"] thead tr th {
    background: #f8f9fc;
    font-weight: 600;
    color: #1a1a2e;
    border-bottom: 2px solid #e8b840;
}

[data-testid="stMetric"] {
    background: white;
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.06);
}

[data-testid="stMetric"] label {
    color: #666;
    font-weight: 500;
    font-size: 13px;
}

[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-weight: 700;
    color: #1a1a2e;
}

[data-testid="stSuccess"] {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border: 1px solid #a5d6a7;
    border-left: 4px solid #4caf50;
    border-radius: 12px;
    padding: 16px 20px;
    color: #1b5e20;
}

[data-testid="stInfo"] {
    background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
    border: 1px solid #90caf9;
    border-left: 4px solid #2196f3;
    border-radius: 12px;
}

[data-testid="stWarning"] {
    background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
    border: 1px solid #ffe082;
    border-left: 4px solid #ffc107;
    border-radius: 12px;
}

[data-testid="stError"] {
    background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
    border: 1px solid #ef9a9a;
    border-left: 4px solid #f44336;
    border-radius: 12px;
}

.stNumberInput input, .stSelectbox select, .stTextInput input {
    border-radius: 10px !important;
    border: 2px solid #e0e0e0 !important;
    padding: 8px 12px !important;
    transition: all 0.3s ease !important;
}

.stNumberInput input:focus, .stSelectbox select:focus, .stTextInput input:focus {
    border-color: #1a1a2e !important;
    box-shadow: 0 0 0 3px rgba(26, 26, 46, 0.1) !important;
}

.stSelectbox > div > div {
    border-radius: 10px !important;
    border: 2px solid #e0e0e0 !important;
}

.stSelectbox > div > div:focus {
    border-color: #1a1a2e !important;
}

.stRadio > div {
    flex-direction: row !important;
    gap: 8px;
}

.stRadio label {
    background: white;
    border: 2px solid #e0e0e0;
    padding: 6px 18px;
    border-radius: 20px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.stRadio label:hover {
    border-color: #1a1a2e;
    background: #f0f4ff;
}

.stRadio label[data-selected="true"] {
    background: #1a1a2e !important;
    color: white !important;
    border-color: #1a1a2e !important;
}

.st-emotion-cache-1kyxreq {
    justify-content: center;
}

.card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,0,0,0.04);
    margin-bottom: 16px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 8px;
}

.card-subtitle {
    font-size: 13px;
    color: #888;
    margin-bottom: 12px;
}

.divider {
    height: 2px;
    background: linear-gradient(90deg, #e8b840 0%, transparent 100%);
    margin: 24px 0;
    border: none;
}

.sidebar-header {
    padding: 24px 16px 16px;
    text-align: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 16px;
}

.sidebar-header h2 {
    color: white;
    font-size: 22px;
    font-weight: 900;
    margin: 0;
    letter-spacing: 1px;
}

.sidebar-header p {
    color: rgba(255,255,255,0.5);
    font-size: 12px;
    margin: 4px 0 0;
}

.gold-badge {
    display: inline-block;
    background: linear-gradient(135deg, #e8b840 0%, #f5a623 100%);
    color: #1a1a2e;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 700;
}

.tag {
    display: inline-block;
    background: #f0f4ff;
    color: #1a1a2e;
    padding: 2px 10px;
    border-radius: 6px;
    font-size: 12px;
    margin: 2px;
}

.score-bar {
    height: 6px;
    border-radius: 3px;
    background: #e0e0e0;
    overflow: hidden;
    margin: 4px 0;
}

.score-bar-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #4caf50, #8bc34a);
    transition: width 0.5s ease;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-in {
    animation: fadeInUp 0.5s ease forwards;
}

.footer {
    text-align: center;
    color: #999;
    font-size: 12px;
    padding: 32px 0 16px;
    border-top: 1px solid #eee;
    margin-top: 48px;
}
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>\U0001f393 高考志愿策略师</h2>
    <p>张雪峰知识框架 · 数据驱动推荐</p>
</div>
""", unsafe_allow_html=True)

PROVINCES = ["北京","天津","河北","山西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","广西","海南","重庆","四川","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆"]

page = st.sidebar.radio("", ["\U0001f3af 志愿推荐","\U0001f9e0 性格测试","\U0001f3eb 院校查询","\U0001f4da 专业查询","\U0001f4ca 数据看板"])
page_key = page.split(" ")[1] if " " in page else page

def get_all_schools():
    return get_merged_schools()

ALL_SCHOOLS = get_all_schools()

def get_all_major_names():
    return sorted([m["name"] for m in MAJORS])

ALL_MAJOR_NAMES = get_all_major_names()

def make_tags(items):
    return "".join(f'<span class="tag">{i.strip()}</span>' for i in items if i.strip())

def get_major_info_by_name(name):
    for m in MAJORS:
        if m["name"] == name:
            return m
    return {}

def format_score_str(scores):
    if not scores: return ""
    timeline = normalize_school({"scores": scores})
    return format_timeline_str(timeline)

def score_to_color(v):
    if v >= 80: return "#4caf50"
    if v >= 60: return "#8bc34a"
    if v >= 40: return "#ffc107"
    if v >= 20: return "#ff9800"
    return "#f44336"

# ========== PAGE: 志愿推荐 ==========
if page_key == "志愿推荐":
    st.markdown("<h1 style='font-size:32px;margin-bottom:4px'>\U0001f3af 志愿推荐</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888;margin-top:0;font-size:15px'>输入你的高考信息，系统将基于张雪峰五层筛选框架为你推荐志愿</p>", unsafe_allow_html=True)

    with st.expander("\U0001f4d6 张雪峰五层筛选框架", expanded=False):
        for level_name, content in ZHANG_XUEFENG_FRAMEWORK.items():
            st.markdown(f"**{level_name}**")
            st.write(content)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">\U0001f9fe 输入信息</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        score = st.number_input("\U0001f4ca 高考分数", min_value=0, max_value=750, value=500, step=1)
        rank = st.number_input("\U0001f4c8 全省排名（位次）", min_value=1, max_value=1000000, value=50000, step=100)
    with col2:
        province = st.selectbox("\U0001f30d 省份", PROVINCES, index=12)
        subject = st.selectbox("\U0001f4d6 文理科", ["理科","文科","新高考"])
        family = st.selectbox("\U0001f3e0 家庭条件", ["普通","有矿","困难"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("\U0001f680 开始分析", type="primary", use_container_width=True):
        subject_map = {"理科": SubjectType.SCIENCE, "文科": SubjectType.LIBERAL_ARTS, "新高考": SubjectType.NEW_GAOKAO}
        family_map = {"有矿": FamilyCondition.RICH, "普通": FamilyCondition.NORMAL, "困难": FamilyCondition.POOR}
        engine = ZhangXuefengEngine()
        student = StudentInput(score=score, province=province, subject=subject_map[subject], rank=rank, family=family_map[family])
        with st.spinner("正在分析..."):
            result = engine.analyze(student)
        summary = result.summary or f"你的分数是{score}分，建议根据位次合理填报。"
        st.success(summary)

        tab1, tab2, tab3, tab4 = st.tabi(["\U0001f3eb 学校推荐", "\U0001f4da 专业推荐", "\U0001f3d8️ 城市推荐", "\U0001f50d 详细分析"])
        with tab1:
            if result.universities:
                data = []
                for u in result.universities:
                    school = ALL_SCHOOLS.get(u.name, {})
                    ranking = get_ranking_ext(u.name)
                    living = get_school_living(u.name)
                    rank_val = ranking.get("软科排名","") if ranking else ""
                    dorm = (living.get("宿舍条件","") or "")[:12] if living else ""
                    data.append({"学校": u.name, "批次": u.tier, "层次": school.get("level",""), "分数": u.score_range, "排名": rank_val, "宿舍": dorm})
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            else:
                st.info("暂无学校推荐数据")

        with tab2:
            if result.majors:
                for m in result.majors[:8]:
                    deep = get_major_deep_analysis_ext(m.name)
                    card = get_major_score_card_ext(m.name)
                    grade = card.get("等级","") if card else ""
                    with st.expander(f"**{m.name}**  就业率 {m.employment_rate}%  薪资 {m.salary_median}元/月  <span class='gold-badge'>{grade}</span>" if grade else f"**{m.name}**  就业率 {m.employment_rate}%  薪资 {m.salary_median}元/月"):
                        ca, cb = st.columns(2)
                        with ca:
                            st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888;font-size:13px">就业率</span> <strong>{m.employment_rate}%</strong></div>', unsafe_allow_html=True)
                            st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888;font-size:13px">薪资中位数</span> <strong>{m.salary_median}元/月</strong></div>', unsafe_allow_html=True)
                            if m.jobs: st.markdown(f'<div><span style="color:#888;font-size:13px">岗位</span> {m.jobs}</div>', unsafe_allow_html=True)
                        with cb:
                            if m.warning: st.warning(m.warning)
                            if deep:
                                sal = deep.get("薪资成长",{})
                                if sal:
                                    parts = [f"{k}:{v}元" for k,v in sal.items()]
                                    st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888;font-size:13px">薪资成长</span><br>{(" " + chr(0x2192) + " ").join(parts)}</div>', unsafe_allow_html=True)
                                st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888;font-size:13px">晋升路径</span><br>{deep.get("晋升路径","")}</div>', unsafe_allow_html=True)
                                st.markdown(f'<div><span style="color:#888;font-size:13px">工作强度</span> {deep.get("工作强度","")}  <span style="color:#888;font-size:13px">35岁危机</span> {deep.get("35岁危机","")}</div>', unsafe_allow_html=True)
            else:
                st.info("暂无专业推荐数据")

        with tab3:
            if result.cities:
                for c in result.cities:
                    st.markdown(f'<div class="card"><strong>{c.city}</strong><br><span style="color:#666">{c.reason}</span></div>', unsafe_allow_html=True)
            else:
                st.info("暂无城市推荐数据")

        with tab4:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="card-title">⚠️ 避坑提示</div>', unsafe_allow_html=True)
                if result.warnings:
                    for w in result.warnings: st.warning(w)
                else: st.info("暂无特别警告")
                st.markdown('<div class="card-title" style="margin-top:16px">\U0001f4c8 录取趋势</div>', unsafe_allow_html=True)
                from gaokao.data.provinces import get_province_batch_lines
                lines = get_province_batch_lines("江西")
                if lines:
                    for year, batches in lines.items():
                        st.markdown(f'<div style="background:#f8f9fc;padding:8px 12px;border-radius:8px;margin-bottom:4px"><strong>{year}年</strong> 一本{batches.get("一本","?")} / 二本{batches.get("二本","?")} / 专科{batches.get("专科","?")}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="card-title">⚠️ 常见陷阱</div>', unsafe_allow_html=True)
                mistakes = get_common_mistakes_ext()
                if mistakes:
                    for key, val in list(mistakes.items())[:5]:
                        st.warning(f"{key}：{val.get('正确做法','')}")
                st.markdown('<div class="card-title" style="margin-top:16px">\U0001f4a1 张雪峰黄金法则</div>', unsafe_allow_html=True)
                for rule in list(get_major_golden_rules().values())[:5]:
                    st.info(rule)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    ca, cb, cc = st.columns(3)
    with ca: st.metric("\U0001f3eb 院校库", f"{len(ALL_SCHOOLS)}+", help="高考志愿策略师库")
    with cb: st.metric("\U0001f4da 专业库", f"{len(ALL_MAJOR_NAMES)}+")
    with cc: st.metric("\U0001f3d8️ 城市库", "50+")

# ========== PAGE: 性格测试 ==========
elif page_key == "性格测试":
    st.markdown("<h1>\U0001f9e0 性格测试</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888;font-size:15px'>回答12个简单问题，找到最适合你性格的专业</p>", unsafe_allow_html=True)

    if "holland_answers" not in st.session_state:
        st.session_state.holland_answers = [0] * 12

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">请回答以下问题</div>', unsafe_allow_html=True)
    answered = sum(st.session_state.holland_answers) if sum(st.session_state.holland_answers) else 0
    st.progress(answered / 12 if answered > 0 else 0.01, text=f"已回答 {answered}/12")
    for i, q in enumerate(PERSONALITY_QUESTIONS):
        ans = st.radio(f"{i+1}. {q['question']}", ["否","是"], index=st.session_state.holland_answers[i], key=f"h_{i}", horizontal=True)
        st.session_state.holland_answers[i] = 1 if ans == "是" else 0
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("\U0001f50d 查看我的性格匹配专业", type="primary", use_container_width=True):
        scores = calculate_holland(st.session_state.holland_answers)
        top_type = max(scores, key=scores.get)
        st.success(f"你的主导性格类型：**{HOLLAND_CODES[top_type]['name_cn']}**  特征：{'、'.join(HOLLAND_CODES[top_type]['traits'])}")
        st.markdown('<div class="card"><div class="card-title">各维度得分</div>', unsafe_allow_html=True)
        cols = st.columns(6)
        for i, (code, info) in enumerate(HOLLAND_CODES.items()):
            with cols[i]:
                val = scores[code]
                st.markdown(f'<div style="text-align:center;padding:12px;background:#f8f9fc;border-radius:12px"><div style="font-size:28px;font-weight:900;color:{score_to_color(val*20)}">{val}</div><div style="font-size:12px;color:#888">{info["name_cn"]}</div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('<div class="card"><div class="card-title">\U0001f4a1 推荐专业</div>', unsafe_allow_html=True)
        majors = recommend_majors_by_holland(scores, top_n=10)
        if majors:
            for major, match_score in majors:
                card = get_major_score_card_ext(major)
                grade = card.get("等级","?") if card else "?"
                total = card.get("总分","?") if card else "?"
                st.markdown(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:#f8f9fc;border-radius:8px;margin-bottom:4px"><span><strong>{major}</strong></span><span><span class="gold-badge">{grade}</span>  {match_score}/6  {total}/100</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">MBTI 参考</div>', unsafe_allow_html=True)
        mbti_type = st.selectbox("如果知道你的 MBTI 类型，在这里选择查看推荐：", list(MBTI_MAJOR_MAP.keys()))
        if mbti_type:
            mbti_info = MBTI_MAJOR_MAP[mbti_type]
            st.markdown(f'<span style="color:#888">{mbti_info["description"]}</span>', unsafe_allow_html=True)
            st.markdown(f'推荐专业：{" 、 ".join(mbti_info["推荐专业"])}', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ========== PAGE: 院校查询 ==========
elif page_key == "院校查询":
    st.markdown("<h1>\U0001f3eb 院校查询</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,1])
    with col1: search = st.text_input("\U0001f50d 搜索学校", placeholder="输入学校名称进行模糊搜索")
    with col2: level_filter = st.selectbox("\U0001f4c4 层次", ["全部","985","211","双一流","本科","民办","专科"])
    with col3: province_filter = st.selectbox("\U0001f30d 省份", ["全部"] + PROVINCES)
    st.markdown("</div>", unsafe_allow_html=True)

    filtered = {}
    for name, school in ALL_SCHOOLS.items():
        if search and search.lower() not in name.lower(): continue
        lv = school.get("level","")
        if level_filter == "985" and "985" not in lv: continue
        if level_filter == "211" and "211" not in lv: continue
        if level_filter == "双一流" and "双一流" not in lv: continue
        if level_filter == "本科" and "本科" not in lv: continue
        if level_filter == "民办" and "民办" not in school.get("nature","") and "民办" not in lv: continue
        if level_filter == "专科" and "专科" not in lv and "高职" not in lv: continue
        if province_filter != "全部":
            sp = school.get("province","") or school.get("province_name","")
            if province_filter not in sp and school.get("city","") != province_filter: continue
        filtered[name] = school

    if filtered:
        st.markdown(f'<div style="text-align:right;color:#888;margin-bottom:8px;font-size:13px">共查找到 <strong>{len(filtered)}</strong> 所学校（显示前 200 所）</div>', unsafe_allow_html=True)
        data = []
        for name, school in list(filtered.items())[:200]:
            ranking = get_ranking_ext(name)
            living = get_school_living(name)
            data.append({"学校": name, "层次": school.get("level",""), "城市": school.get("city",""), "分数": format_score_str(school.get("scores",{})), "排名": ranking.get("软科排名","") if ranking else "", "宿舍": (living.get("宿舍条件","") or "")[:12] if living else ""})
        st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
    else:
        st.info("未找到匹配的学校，请调整筛选条件")

# ========== PAGE: 专业查询 ==========
elif page_key == "专业查询":
    st.markdown("<h1>\U0001f4da 专业查询</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2,1])
    with col1: major_search = st.text_input("\U0001f50d 搜索专业", placeholder="输入专业名称")
    with col2: selected_major = st.selectbox("\U0001f4c4 或选择专业", ["请选择"] + ALL_MAJOR_NAMES)
    st.markdown("</div>", unsafe_allow_html=True)

    major_name = selected_major if selected_major != "请选择" else ""
    if major_search:
        matches = [m for m in ALL_MAJOR_NAMES if major_search.lower() in m.lower()]
        if matches:
            major_name = st.radio("匹配结果：", matches, horizontal=True) if len(matches) > 1 else matches[0]

    if major_name:
        info = get_major_info_by_name(major_name)
        if info:
            st.markdown(f'<h2 style="margin-top:0">{major_name}</h2>', unsafe_allow_html=True)
            ca, cb = st.columns(2)
            with ca:
                st.markdown('<div class="card"><div class="card-title">\U0001f4c8 基本信息</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f0f0f0"><span style="color:#888">就业率</span><strong>{info.get("employment_rate","?")}%</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f0f0f0"><span style="color:#888">薪资中位数</span><strong>{info.get("salary_median","?")}元/月</strong></div>', unsafe_allow_html=True)
                if info.get("jobs"): st.markdown(f'<div style="padding:6px 0"><span style="color:#888">就业方向</span><br>{make_tags(info["jobs"].split(","))}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with cb:
                deep = get_major_deep_analysis_ext(major_name)
                if deep:
                    st.markdown('<div class="card"><div class="card-title">\U0001f4c9 薪资成长曲线</div>', unsafe_allow_html=True)
                    salaries = deep.get("薪资成长",{})
                    if salaries:
                        chart_data = pd.DataFrame({"阶段": list(salaries.keys()), "月薪(元)": list(salaries.values())})
                        st.bar_chart(chart_data.set_index("阶段"), height=150)
                    st.markdown(f'<div style="margin-top:8px"><span style="color:#888;font-size:13px">晋升路径</span><br>{deep.get("晋升路径","")}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div style="margin-top:4px"><span style="color:#888;font-size:13px">工作强度</span> {deep.get("工作强度","")}  <span style="color:#888;font-size:13px">35岁危机</span> {deep.get("35岁危机","")}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            emp = get_major_employment_deep_ext(major_name)
            if emp:
                st.markdown('<div class="card"><div class="card-title">\U0001f3e2 分层就业数据</div>', unsafe_allow_html=True)
                emp_data = pd.DataFrame({
                    "层次": ["985","211","双非"],
                    "就业率": [f"{emp.get('就业率_985',0)*100:.0f}%", f"{emp.get('就业率_211',0)*100:.0f}%", f"{emp.get('就业率_双非',0)*100:.0f}%"],
                    "平均薪资": [f"{emp.get('薪资_985',0)}元", f"{emp.get('薪资_211',0)}元", f"{emp.get('薪资_双非',0)}元"],
                })
                st.dataframe(emp_data, hide_index=True, use_container_width=True)
                if emp.get("头部公司"):
                    st.markdown(f'<div style="margin-top:8px"><span style="color:#888">头部公司</span>: {make_tags(emp["头部公司"])}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            city_m = get_major_city_match_ext(major_name)
            if city_m:
                st.markdown('<div class="card"><div class="card-title">\U0001f30d 最佳就业城市</div>', unsafe_allow_html=True)
                all_cities = []
                for tier, cities in city_m.items():
                    for c in cities:
                        c["tier"] = tier
                        all_cities.append(c)
                city_df = pd.DataFrame(all_cities)
                if not city_df.empty:
                    st.dataframe(city_df[["city","tier","avg_salary","reason"]].rename(columns={"city":"城市","tier":"梯队","avg_salary":"平均薪资","reason":"原因"}), hide_index=True, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            card = get_major_score_card_ext(major_name)
            if card:
                st.markdown('<div class="card"><div class="card-title">⭐ 综合评分</div>', unsafe_allow_html=True)
                cols = st.columns(7)
                dims = ["就业率","薪资水平","工作强度","35岁危机","行业前景","转行难度","考研收益"]
                for i, d in enumerate(dims):
                    v = card.get(d, 0)
                    with cols[i]:
                        st.markdown(f'<div style="text-align:center;padding:8px;background:#f8f9fc;border-radius:8px"><div style="font-size:20px;font-weight:700;color:{score_to_color(v)}">{v}</div><div style="font-size:11px;color:#888;margin-top:2px">{d}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="text-align:center;margin-top:12px;font-size:18px"><strong>总分：{card.get("总分","?")}/100</strong>  <span class="gold-badge">{card.get("等级","?")}</span></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            path = get_career_path(major_name)
            if path:
                st.markdown('<div class="card"><div class="card-title">\U0001f6e4️ 20年职业路径模拟</div>', unsafe_allow_html=True)
                for stage, detail in path.get("典型路径",{}).items():
                    st.markdown(f'<div style="background:#f8f9fc;padding:10px 14px;border-radius:10px;margin-bottom:6px;border-left:3px solid #e8b840"><strong>{stage}</strong> {detail.get("职位","")} | 年薪{detail.get("年薪","")}<br><span style="color:#888;font-size:13px">{detail.get("状态","")}</span></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            match = get_school_major_match_ext(major_name)
            if match:
                st.markdown('<div class="card"><div class="card-title">\U0001f3c6 推荐院校</div>', unsafe_allow_html=True)
                for tier, schools in match.items():
                    if tier in ("第一梯队","第二梯队","第三梯队"):
                        st.markdown(f'<div style="margin-bottom:6px"><span style="color:#888;font-size:13px">{tier}</span> {make_tags(schools)}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning(f"暂未收录「{major_name}」的详细信息")
    else:
        st.info("请搜索或选择一个专业查看详情")

# ========== PAGE: 数据看板 ==========
elif page_key == "数据看板":
    st.markdown("<h1>\U0001f4ca 数据看板</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888;font-size:15px'>知识库数据统计与可视化</p>", unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]: st.metric("\U0001f3eb 院校总数", f"{len(ALL_SCHOOLS)}+", delta="1500+")
    with cols[1]: st.metric("\U0001f4da 专业总数", f"{len(ALL_MAJOR_NAMES)}+", delta="111+")
    with cols[2]: st.metric("\U0001f3d8️ 城市数据", "50+", delta="31省")
    with cols[3]: st.metric("\U0001f4c8 行业分析", "40+", delta="全面覆盖")

    st.markdown('<div class="card"><div class="card-title">\U0001f4dd 数据质量</div>', unsafe_allow_html=True)
    cs = coverage_statistics()
    qa, qb, qc = st.columns(3)
    with qa: st.metric("\U0001f4c6 院校总数", f"{cs['total']}所", delta="合并两个数据源")
    with qb: st.metric("\U0001f4c5 2025官方", f"{cs['by_year']['2025']['official']}所", delta="有真实2025数据")
    with qc: st.metric("\U0001f52e 2025缺失", f"{cs['by_year']['2025']['missing']}所", delta="需要补数据")
    st.markdown('<div style="color:#888;font-size:12px">院校查询和志愿推荐中，官方/估算/缺失会分别标注</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><div class="card-title">\U0001f3eb 院校层次分布</div>', unsafe_allow_html=True)
        level_counts = {}
        for school in ALL_SCHOOLS.values():
            lv = school.get("level","未知")
            level_counts[lv] = level_counts.get(lv, 0) + 1
        if level_counts:
            st.bar_chart(pd.DataFrame({"层次": list(level_counts.keys()), "数量": list(level_counts.values())}).set_index("层次"), height=250)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="card-title">\U0001f4da 专业推荐分类</div>', unsafe_allow_html=True)
        class_data = []
        for tier, majors in ZHANG_XUEFENG_MAJOR_CATEGORIES.items():
            class_data.append({"分类": tier, "数量": len(majors)})
        if class_data:
            st.bar_chart(pd.DataFrame(class_data).set_index("分类"), height=250, color="#e8b840")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">\U0001f4b0 奖学金体系</div>', unsafe_allow_html=True)
    sch_data = [{"类型": name, "金额": info.get("金额",""), "比例": info.get("比例","")} for name, info in SCHOLARSHIP_TYPES.items()]
    if sch_data:
        st.dataframe(pd.DataFrame(sch_data), hide_index=True, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">\U0001f3e0 家庭财务规划建议</div>', unsafe_allow_html=True)
    for tier, plan in FINANCIAL_PLANNING.items():
        with st.expander(tier):
            st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888">策略</span> {plan.get("策略","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888">月预算</span> {plan.get("月预算","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="margin-bottom:4px"><span style="color:#888">推荐路径</span> {", ".join(plan.get("推荐路径",[]))}</div>', unsafe_allow_html=True)
            if plan.get("避坑"): st.warning(f"避坑：{plan.get('避坑','')}")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="footer">\U0001f393 高考志愿策略师 - 基于张雪峰知识框架 | 数据来源：掌上高考</div>', unsafe_allow_html=True)
