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

st.set_page_config(page_title="高考志愿策略师", page_icon="🎓", layout="wide")

# ========== STUNNING CSS ==========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');

* { font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    color: #e2e8f0;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617 0%, #0f172a 50%, #1e293b 100%);
    border-right: 1px solid rgba(255,255,255,0.05);
}

[data-testid="stSidebar"] .stTitle, 
[data-testid="stSidebar"] .stMarkdown { color: white !important; }

[data-testid="stSidebar"] .stRadio > div { gap: 6px; }

[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.03);
    color: rgba(255,255,255,0.7);
    padding: 14px 18px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-weight: 400;
    cursor: pointer;
    backdrop-filter: blur(10px);
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.08);
    color: white;
    border-color: rgba(232, 184, 64, 0.3);
    transform: translateX(6px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

[data-testid="stSidebar"] .stRadio label[data-selected="true"] {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%) !important;
    color: #0f172a !important;
    border-color: #e8b840 !important;
    font-weight: 700;
    box-shadow: 0 4px 20px rgba(232, 184, 64, 0.4);
    transform: translateX(6px);
}

/* ===== MAIN CONTENT ===== */
h1, h2, h3 { font-weight: 700 !important; letter-spacing: -0.02em; }

.stApp h1 {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 50%, #e8b840 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 42px !important;
    font-weight: 900 !important;
    margin-bottom: 8px !important;
}

.stApp p { color: #94a3b8; font-size: 15px; }

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%);
    color: #0f172a !important;
    border: none;
    padding: 14px 36px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 20px rgba(232, 184, 64, 0.3);
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(232, 184, 64, 0.5);
    background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
}

.stButton > button:active { transform: translateY(0); }

/* ===== CARDS ===== */
.card {
    background: rgba(30, 41, 59, 0.8);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    border-color: rgba(232, 184, 64, 0.2);
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #e8b840;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-subtitle {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 16px;
}

/* ===== EXPANDERS ===== */
div[data-testid="stExpander"] {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    margin-bottom: 12px;
    overflow: hidden;
}

div[data-testid="stExpander"] > div:first-child {
    background: rgba(30, 41, 59, 0.8);
    border-radius: 16px;
    padding: 4px 16px;
}

div[data-testid="stExpander"] > div:first-child:hover {
    background: rgba(30, 41, 59, 1);
}

/* ===== TABS ===== */
[data-testid="stTab"] {
    background: rgba(30, 41, 59, 0.6);
    border-radius: 12px 12px 0 0;
    padding: 10px 28px;
    font-weight: 500;
    color: #94a3b8;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-bottom: none;
}

[data-testid="stTab"][aria-selected="true"] {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%);
    color: #0f172a !important;
    font-weight: 700;
    box-shadow: 0 -4px 20px rgba(232, 184, 64, 0.3);
}

/* ===== DATA TABLE ===== */
[data-testid="stDataFrame"] {
    background: rgba(15, 23, 42, 0.9);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    overflow: hidden;
}

[data-testid="stDataFrame"] thead tr th {
    background: rgba(232, 184, 64, 0.1);
    font-weight: 600;
    color: #e8b840;
    border-bottom: 2px solid #e8b840;
}

[data-testid="stDataFrame"] tbody tr { background: rgba(30, 41, 59, 0.6); }
[data-testid="stDataFrame"] tbody tr:hover { background: rgba(232, 184, 64, 0.05); }

/* ===== METRICS ===== */
[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.08);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    border-color: rgba(232, 184, 64, 0.3);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

[data-testid="stMetric"] label { color: #94a3b8; font-weight: 500; font-size: 14px; }
[data-testid="stMetric"] [data-testid="stMetricValue"] { font-weight: 900; color: #e8b840; }

/* ===== FORM INPUTS ===== */
.stNumberInput input, .stSelectbox select, .stTextInput input {
    background: rgba(15, 23, 42, 0.8) !important;
    border-radius: 12px !important;
    border: 2px solid rgba(255, 255, 255, 0.1) !important;
    padding: 12px 16px !important;
    color: #e2e8f0 !important;
    transition: all 0.3s ease !important;
}

.stNumberInput input:focus, .stSelectbox select:focus, .stTextInput input:focus {
    border-color: #e8b840 !important;
    box-shadow: 0 0 0 3px rgba(232, 184, 64, 0.2) !important;
}

.stSelectbox > div > div {
    background: rgba(15, 23, 42, 0.8) !important;
    border-radius: 12px !important;
    border: 2px solid rgba(255, 255, 255, 0.1) !important;
    color: #e2e8f0 !important;
}

/* ===== RADIO BUTTONS ===== */
.stRadio > div { flex-direction: row !important; gap: 8px; }

.stRadio label {
    background: rgba(30, 41, 59, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.1);
    padding: 8px 20px;
    border-radius: 24px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
    color: #94a3b8;
}

.stRadio label:hover {
    border-color: #e8b840;
    background: rgba(232, 184, 64, 0.1);
    color: #e8b840;
}

.stRadio label[data-selected="true"] {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%) !important;
    color: #0f172a !important;
    border-color: #e8b840 !important;
    font-weight: 600;
}

/* ===== ALERTS ===== */
[data-testid="stSuccess"] {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
    border: 1px solid rgba(34, 197, 94, 0.3);
    border-left: 4px solid #22c55e;
    border-radius: 12px;
    color: #4ade80;
}

[data-testid="stInfo"] {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%);
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-left: 4px solid #3b82f6;
    border-radius: 12px;
    color: #60a5fa;
}

[data-testid="stWarning"] {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-left: 4px solid #f59e0b;
    border-radius: 12px;
    color: #fbbf24;
}

[data-testid="stError"] {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
    border: 1px solid rgba(239, 68, 68, 0.3);
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    color: #f87171;
}

/* ===== SPECIAL ELEMENTS ===== */
.gold-badge {
    display: inline-block;
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%);
    color: #0f172a;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.tag {
    display: inline-block;
    background: rgba(232, 184, 64, 0.1);
    color: #e8b840;
    padding: 4px 12px;
    border-radius: 8px;
    font-size: 12px;
    margin: 3px;
    border: 1px solid rgba(232, 184, 64, 0.2);
    transition: all 0.2s ease;
}

.tag:hover {
    background: rgba(232, 184, 64, 0.2);
    transform: translateY(-1px);
}

.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent 0%, #e8b840 50%, transparent 100%);
    margin: 32px 0;
    border: none;
}

.sidebar-header {
    padding: 28px 16px 20px;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 20px;
}

.sidebar-header h2 {
    background: linear-gradient(135deg, #e8b840 0%, #f59e0b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 24px;
    font-weight: 900;
    margin: 0;
    letter-spacing: 1px;
}

.sidebar-header p {
    color: #64748b;
    font-size: 12px;
    margin: 6px 0 0;
}

.score-bar {
    height: 8px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.1);
    overflow: hidden;
    margin: 6px 0;
}

.score-bar-fill {
    height: 100%;
    border-radius: 4px;
    background: linear-gradient(90deg, #22c55e, #86efac);
    transition: width 0.5s ease;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.animate-in { animation: fadeInUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards; }

.footer {
    text-align: center;
    color: #475569;
    font-size: 13px;
    padding: 40px 0 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    margin-top: 60px;
}

/* ===== PROGRESS BAR ===== */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #e8b840, #f59e0b) !important;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.5); }
::-webkit-scrollbar-thumb { background: rgba(232, 184, 64, 0.3); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(232, 184, 64, 0.5); }
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>🎓 高考志愿策略师</h2>
    <p>张雪峰知识框架 · 数据驱动推荐</p>
</div>
""", unsafe_allow_html=True)

PROVINCES = ["北京","天津","河北","山西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","广西","海南","重庆","四川","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆"]

page = st.sidebar.radio("", ["🎯 志愿推荐","🧠 性格测试","🏫 院校查询","📚 专业查询","📊 数据看板"])
page_key = page.split(" ")[1] if " " in page else page

def get_all_schools():
    schools = {}
    for u in JIANGXI_DATA:
        name = u.get("name","")
        if name:
            schools[name] = {"name": name, "level": u.get("level",""), "city": u.get("city",""), "type": u.get("type",""), "nature": u.get("nature",""), "scores": u.get("scores",{}), "strong_majors": u.get("strong_majors",[])}
    for u in get_extra_universities():
        name = u.get("name","")
        if name and name not in schools:
            schools[name] = {"name": name, "level": u.get("level",""), "city": u.get("city",""), "type": u.get("type",""), "scores": u.get("scores",{})}
    return schools

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
    parts = []
    for y in sorted(scores.keys()):
        s = scores[y]
        v = s.get("min") if isinstance(s, dict) else s
        if v: parts.append(f"{y}:{v}分")
    return "、".join(parts)

def score_to_color(v):
    if v >= 80: return "#22c55e"
    if v >= 60: return "#86efac"
    if v >= 40: return "#fbbf24"
    if v >= 20: return "#fb923c"
    return "#f87171"

# ========== PAGE: 志愿推荐 ==========
if page_key == "志愿推荐":
    st.markdown("<h1>🎯 志愿推荐</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;margin-top:0;font-size:16px'>输入你的高考信息，系统将基于张雪峰五层筛选框架为你推荐志愿</p>", unsafe_allow_html=True)

    with st.expander("📖 张雪峰五层筛选框架", expanded=False):
        for level_name, content in ZHANG_XUEFENG_FRAMEWORK.items():
            st.markdown(f"**{level_name}**")
            st.write(content)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📝 输入信息</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        score = st.number_input("📊 高考分数", min_value=0, max_value=750, value=500, step=1)
        rank = st.number_input("📈 全省排名（位次）", min_value=1, max_value=1000000, value=50000, step=100)
    with col2:
        province = st.selectbox("🌍 省份", PROVINCES, index=12)
        subject = st.selectbox("📖 文理科", ["理科","文科","新高考"])
        family = st.selectbox("🏠 家庭条件", ["普通","有矿","困难"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚀 开始分析", type="primary", use_container_width=True):
        subject_map = {"理科": SubjectType.SCIENCE, "文科": SubjectType.LIBERAL_ARTS, "新高考": SubjectType.NEW_GAOKAO}
        family_map = {"有矿": FamilyCondition.RICH, "普通": FamilyCondition.NORMAL, "困难": FamilyCondition.POOR}
        engine = ZhangXuefengEngine()
        student = StudentInput(score=score, province=province, subject=subject_map[subject], rank=rank, family=family_map[family])
        with st.spinner("正在分析..."):
            result = engine.analyze(student)
        summary = result.summary or f"你的分数是{score}分，建议根据位次合理填报。"
        st.success(summary)

        tab1, tab2, tab3, tab4 = st.tabs(["🏫 学校推荐", "📚 专业推荐", "🏙️ 城市推荐", "🔍 详细分析"])
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
                    with st.expander(f"**{m.name}**  ⭐ {m.employment_rate}%  💰 {m.salary_median}元/月  <span class='gold-badge'>{grade}</span>" if grade else f"**{m.name}**  ⭐ {m.employment_rate}%  💰 {m.salary_median}元/月"):
                        ca, cb = st.columns(2)
                        with ca:
                            st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8;font-size:13px">就业率</span> <strong style="color:#22c55e">{m.employment_rate}%</strong></div>', unsafe_allow_html=True)
                            st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8;font-size:13px">薪资中位数</span> <strong style="color:#e8b840">{m.salary_median}元/月</strong></div>', unsafe_allow_html=True)
                            if m.jobs: st.markdown(f'<div><span style="color:#94a3b8;font-size:13px">岗位</span> {m.jobs}</div>', unsafe_allow_html=True)
                        with cb:
                            if m.warning: st.warning(m.warning)
                            if deep:
                                sal = deep.get("薪资成长",{})
                                if sal:
                                    parts = [f"{k}:{v}元" for k,v in sal.items()]
                                    st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8;font-size:13px">薪资成长</span><br>{(" " + chr(0x2192) + " ").join(parts)}</div>', unsafe_allow_html=True)
                                st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8;font-size:13px">晋升路径</span><br>{deep.get("晋升路径","")}</div>', unsafe_allow_html=True)
                                st.markdown(f'<div><span style="color:#94a3b8;font-size:13px">工作强度</span> {deep.get("工作强度","")}  <span style="color:#94a3b8;font-size:13px">35岁危机</span> {deep.get("35岁危机","")}</div>', unsafe_allow_html=True)
            else:
                st.info("暂无专业推荐数据")

        with tab3:
            if result.cities:
                for c in result.cities:
                    st.markdown(f'<div class="card"><strong style="color:#e8b840">{c.city}</strong><br><span style="color:#94a3b8">{c.reason}</span></div>', unsafe_allow_html=True)
            else:
                st.info("暂无城市推荐数据")

        with tab4:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="card-title">⚠️ 避坑提示</div>', unsafe_allow_html=True)
                if result.warnings:
                    for w in result.warnings: st.warning(w)
                else: st.info("暂无特别警告")
                st.markdown('<div class="card-title" style="margin-top:20px">📈 录取趋势</div>', unsafe_allow_html=True)
                from gaokao.data.provinces import get_province_batch_lines
                lines = get_province_batch_lines("江西")
                if lines:
                    for year, batches in lines.items():
                        st.markdown(f'<div style="background:rgba(30, 41, 59, 0.6);padding:12px 16px;border-radius:12px;margin-bottom:8px;border-left:3px solid #e8b840"><strong>{year}年</strong> 一本{batches.get("一本","?")} / 二本{batches.get("二本","?")} / 专科{batches.get("专科","?")}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="card-title">⚠️ 常见陷阱</div>', unsafe_allow_html=True)
                mistakes = get_common_mistakes_ext()
                if mistakes:
                    for key, val in list(mistakes.items())[:5]:
                        st.warning(f"{key}：{val.get('正确做法','')}")
                st.markdown('<div class="card-title" style="margin-top:20px">💡 张雪峰黄金法则</div>', unsafe_allow_html=True)
                for rule in list(get_major_golden_rules().values())[:5]:
                    st.info(rule)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    ca, cb, cc = st.columns(3)
    with ca: st.metric("🏫 院校库", f"{len(ALL_SCHOOLS)}+", help="高考志愿策略师库")
    with cb: st.metric("📚 专业库", f"{len(ALL_MAJOR_NAMES)}+")
    with cc: st.metric("🏙️ 城市库", "50+")

# ========== PAGE: 性格测试 ==========
elif page_key == "性格测试":
    st.markdown("<h1>🧠 性格测试</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;font-size:16px'>回答12个简单问题，找到最适合你性格的专业</p>", unsafe_allow_html=True)

    if "holland_answers" not in st.session_state:
        st.session_state.holland_answers = [0] * 12

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📝 请回答以下问题</div>', unsafe_allow_html=True)
    answered = sum(st.session_state.holland_answers) if sum(st.session_state.holland_answers) else 0
    st.progress(answered / 12 if answered > 0 else 0.01, text=f"已回答 {answered}/12")
    for i, q in enumerate(PERSONALITY_QUESTIONS):
        ans = st.radio(f"{i+1}. {q['question']}", ["否","是"], index=st.session_state.holland_answers[i], key=f"h_{i}", horizontal=True)
        st.session_state.holland_answers[i] = 1 if ans == "是" else 0
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔍 查看我的性格匹配专业", type="primary", use_container_width=True):
        scores = calculate_holland(st.session_state.holland_answers)
        top_type = max(scores, key=scores.get)
        st.success(f"你的主导性格类型：**{HOLLAND_CODES[top_type]['name_cn']}**  特征：{'、'.join(HOLLAND_CODES[top_type]['traits'])}")
        st.markdown('<div class="card"><div class="card-title">📊 各维度得分</div>', unsafe_allow_html=True)
        cols = st.columns(6)
        for i, (code, info) in enumerate(HOLLAND_CODES.items()):
            with cols[i]:
                val = scores[code]
                st.markdown(f'<div style="text-align:center;padding:16px;background:rgba(15, 23, 42, 0.6);border-radius:16px;border:1px solid rgba(255,255,255,0.05)"><div style="font-size:32px;font-weight:900;color:{score_to_color(val*20)}">{val}</div><div style="font-size:13px;color:#94a3b8;margin-top:4px">{info["name_cn"]}</div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('<div class="card"><div class="card-title">💡 推荐专业</div>', unsafe_allow_html=True)
        majors = recommend_majors_by_holland(scores, top_n=10)
        if majors:
            for major, match_score in majors:
                card = get_major_score_card_ext(major)
                grade = card.get("等级","?") if card else "?"
                total = card.get("总分","?") if card else "?"
                st.markdown(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 16px;background:rgba(15, 23, 42, 0.6);border-radius:12px;margin-bottom:8px;border:1px solid rgba(255,255,255,0.05)"><span><strong style="color:#e8b840">{major}</strong></span><span><span class="gold-badge">{grade}</span>  {match_score}/6  {total}/100</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">🎭 MBTI 参考</div>', unsafe_allow_html=True)
        mbti_type = st.selectbox("如果知道你的 MBTI 类型，在这里选择查看推荐：", list(MBTI_MAJOR_MAP.keys()))
        if mbti_type:
            mbti_info = MBTI_MAJOR_MAP[mbti_type]
            st.markdown(f'<span style="color:#94a3b8">{mbti_info["description"]}</span>', unsafe_allow_html=True)
            st.markdown(f'推荐专业：{" 、 ".join(mbti_info["推荐专业"])}', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ========== PAGE: 院校查询 ==========
elif page_key == "院校查询":
    st.markdown("<h1>🏫 院校查询</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,1])
    with col1: search = st.text_input("🔍 搜索学校", placeholder="输入学校名称进行模糊搜索")
    with col2: level_filter = st.selectbox("📄 层次", ["全部","985","211","双一流","本科","民办","专科"])
    with col3: province_filter = st.selectbox("🌍 省份", ["全部"] + PROVINCES)
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
        st.markdown(f'<div style="text-align:right;color:#64748b;margin-bottom:12px;font-size:13px">共查找到 <strong style="color:#e8b840">{len(filtered)}</strong> 所学校（显示前 200 所）</div>', unsafe_allow_html=True)
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
    st.markdown("<h1>📚 专业查询</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2,1])
    with col1: major_search = st.text_input("🔍 搜索专业", placeholder="输入专业名称")
    with col2: selected_major = st.selectbox("📄 或选择专业", ["请选择"] + ALL_MAJOR_NAMES)
    st.markdown("</div>", unsafe_allow_html=True)

    major_name = selected_major if selected_major != "请选择" else ""
    if major_search:
        matches = [m for m in ALL_MAJOR_NAMES if major_search.lower() in m.lower()]
        if matches:
            major_name = st.radio("匹配结果：", matches, horizontal=True) if len(matches) > 1 else matches[0]

    if major_name:
        info = get_major_info_by_name(major_name)
        if info:
            st.markdown(f'<h2 style="margin-top:0;color:#e8b840">{major_name}</h2>', unsafe_allow_html=True)
            ca, cb = st.columns(2)
            with ca:
                st.markdown('<div class="card"><div class="card-title">📈 基本信息</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.05)"><span style="color:#94a3b8">就业率</span><strong style="color:#22c55e">{info.get("employment_rate","?")}%</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.05)"><span style="color:#94a3b8">薪资中位数</span><strong style="color:#e8b840">{info.get("salary_median","?")}元/月</strong></div>', unsafe_allow_html=True)
                if info.get("jobs"): st.markdown(f'<div style="padding:8px 0"><span style="color:#94a3b8">就业方向</span><br>{make_tags(info["jobs"].split(","))}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with cb:
                deep = get_major_deep_analysis_ext(major_name)
                if deep:
                    st.markdown('<div class="card"><div class="card-title">📉 薪资成长曲线</div>', unsafe_allow_html=True)
                    salaries = deep.get("薪资成长",{})
                    if salaries:
                        chart_data = pd.DataFrame({"阶段": list(salaries.keys()), "月薪(元)": list(salaries.values())})
                        st.bar_chart(chart_data.set_index("阶段"), height=180)
                    st.markdown(f'<div style="margin-top:12px"><span style="color:#94a3b8;font-size:13px">晋升路径</span><br>{deep.get("晋升路径","")}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div style="margin-top:8px"><span style="color:#94a3b8;font-size:13px">工作强度</span> {deep.get("工作强度","")}  <span style="color:#94a3b8;font-size:13px">35岁危机</span> {deep.get("35岁危机","")}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            emp = get_major_employment_deep_ext(major_name)
            if emp:
                st.markdown('<div class="card"><div class="card-title">🏢 分层就业数据</div>', unsafe_allow_html=True)
                emp_data = pd.DataFrame({
                    "层次": ["985","211","双非"],
                    "就业率": [f"{emp.get('就业率_985',0)*100:.0f}%", f"{emp.get('就业率_211',0)*100:.0f}%", f"{emp.get('就业率_双非',0)*100:.0f}%"],
                    "平均薪资": [f"{emp.get('薪资_985',0)}元", f"{emp.get('薪资_211',0)}元", f"{emp.get('薪资_双非',0)}元"],
                })
                st.dataframe(emp_data, hide_index=True, use_container_width=True)
                if emp.get("头部公司"):
                    st.markdown(f'<div style="margin-top:12px"><span style="color:#94a3b8">头部公司</span>: {make_tags(emp["头部公司"])}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            city_m = get_major_city_match_ext(major_name)
            if city_m:
                st.markdown('<div class="card"><div class="card-title">🌍 最佳就业城市</div>', unsafe_allow_html=True)
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
                        st.markdown(f'<div style="text-align:center;padding:12px;background:rgba(15, 23, 42, 0.6);border-radius:12px;border:1px solid rgba(255,255,255,0.05)"><div style="font-size:24px;font-weight:700;color:{score_to_color(v)}">{v}</div><div style="font-size:11px;color:#94a3b8;margin-top:4px">{d}</div></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="text-align:center;margin-top:16px;font-size:20px"><strong style="color:#e8b840">总分：{card.get("总分","?")}/100</strong>  <span class="gold-badge">{card.get("等级","?")}</span></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            path = get_career_path(major_name)
            if path:
                st.markdown('<div class="card"><div class="card-title">🚂 20年职业路径模拟</div>', unsafe_allow_html=True)
                for stage, detail in path.get("典型路径",{}).items():
                    st.markdown(f'<div style="background:rgba(30, 41, 59, 0.6);padding:14px 18px;border-radius:12px;margin-bottom:8px;border-left:4px solid #e8b840"><strong style="color:#e8b840">{stage}</strong> {detail.get("职位","")} | 年薪{detail.get("年薪","")}<br><span style="color:#94a3b8;font-size:13px">{detail.get("状态","")}</span></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            match = get_school_major_match_ext(major_name)
            if match:
                st.markdown('<div class="card"><div class="card-title">🏆 推荐院校</div>', unsafe_allow_html=True)
                for tier, schools in match.items():
                    if tier in ("第一梯队","第二梯队","第三梯队"):
                        st.markdown(f'<div style="margin-bottom:8px"><span style="color:#94a3b8;font-size:13px">{tier}</span> {make_tags(schools)}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning(f"暂未收录「{major_name}」的详细信息")
    else:
        st.info("请搜索或选择一个专业查看详情")

# ========== PAGE: 数据看板 ==========
elif page_key == "数据看板":
    st.markdown("<h1>📊 数据看板</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;font-size:16px'>知识库数据统计与可视化</p>", unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]: st.metric("🏫 院校总数", f"{len(ALL_SCHOOLS)}+", delta="1500+")
    with cols[1]: st.metric("📚 专业总数", f"{len(ALL_MAJOR_NAMES)}+", delta="111+")
    with cols[2]: st.metric("🏙️ 城市数据", "50+", delta="31省")
    with cols[3]: st.metric("📈 行业分析", "40+", delta="全面覆盖")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><div class="card-title">🏫 院校层次分布</div>', unsafe_allow_html=True)
        level_counts = {}
        for school in ALL_SCHOOLS.values():
            lv = school.get("level","未知")
            level_counts[lv] = level_counts.get(lv, 0) + 1
        if level_counts:
            st.bar_chart(pd.DataFrame({"层次": list(level_counts.keys()), "数量": list(level_counts.values())}).set_index("层次"), height=280)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="card-title">📚 专业推荐分类</div>', unsafe_allow_html=True)
        class_data = []
        for tier, majors in ZHANG_XUEFENG_MAJOR_CATEGORIES.items():
            class_data.append({"分类": tier, "数量": len(majors)})
        if class_data:
            st.bar_chart(pd.DataFrame(class_data).set_index("分类"), height=280, color="#e8b840")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">💰 奖学金体系</div>', unsafe_allow_html=True)
    sch_data = [{"类型": name, "金额": info.get("金额",""), "比例": info.get("比例","")} for name, info in SCHOLARSHIP_TYPES.items()]
    if sch_data:
        st.dataframe(pd.DataFrame(sch_data), hide_index=True, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">🏠 家庭财务规划建议</div>', unsafe_allow_html=True)
    for tier, plan in FINANCIAL_PLANNING.items():
        with st.expander(tier):
            st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8">策略</span> {plan.get("策略","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8">月预算</span> {plan.get("月预算","")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="margin-bottom:6px"><span style="color:#94a3b8">推荐路径</span> {", ".join(plan.get("推荐路径",[]))}</div>', unsafe_allow_html=True)
            if plan.get("避坑"): st.warning(f"避坑：{plan.get('避坑','')}")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="footer">🎓 高考志愿策略师 - 基于张雪峰知识框架 | 数据来源：掌上高考</div>', unsafe_allow_html=True)
