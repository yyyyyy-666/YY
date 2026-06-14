INDUSTRY_TRENDS = {
    "互联网": {"trend": "稳定", "growth": "5%", "avg_salary": 15000, "outlook": "AI 驱动增长，传统岗位竞争加剧"},
    "人工智能": {"trend": "高速增长", "growth": "25%", "avg_salary": 20000, "outlook": "人才缺口大，薪资持续上涨"},
    "半导体": {"trend": "高速增长", "growth": "20%", "avg_salary": 18000, "outlook": "国产替代驱动，人才需求旺盛"},
    "新能源": {"trend": "高速增长", "growth": "30%", "avg_salary": 12000, "outlook": "光伏、储能、新能源车三大方向"},
    "新能源车": {"trend": "高速增长", "growth": "35%", "avg_salary": 13000, "outlook": "渗透率持续提升，人才需求大"},
    "医疗健康": {"trend": "稳定增长", "growth": "10%", "avg_salary": 10000, "outlook": "老龄化驱动，长期看好"},
    "金融": {"trend": "稳定", "growth": "3%", "avg_salary": 12000, "outlook": "AI 冲击传统岗位，量化/金融科技机会多"},
    "教育": {"trend": "调整", "growth": "-5%", "avg_salary": 7000, "outlook": "政策影响大，但 AI 教育是新方向"},
    "制造": {"trend": "转型升级", "growth": "8%", "avg_salary": 9000, "outlook": "智能制造驱动，自动化人才需求增加"},
    "建筑": {"trend": "下行", "growth": "-10%", "avg_salary": 8000, "outlook": "房地产下行，但基建仍有需求"},
    "房地产": {"trend": "下行", "growth": "-15%", "avg_salary": 8000, "outlook": "行业调整期，短期不乐观"},
    "电商": {"trend": "稳定增长", "growth": "12%", "avg_salary": 10000, "outlook": "直播电商、跨境电商是增长点"},
    "游戏": {"trend": "稳定", "growth": "5%", "avg_salary": 13000, "outlook": "AI 辅助开发，但行业监管严格"},
    "传媒": {"trend": "转型", "growth": "0%", "avg_salary": 7000, "outlook": "传统媒体衰落，新媒体/AI 内容是方向"},
    "汽车": {"trend": "转型升级", "growth": "10%", "avg_salary": 11000, "outlook": "电动化、智能化转型，软件人才需求增加"},
    "电力": {"trend": "稳定", "growth": "5%", "avg_salary": 10000, "outlook": "新能源并网、智能电网是增长点"},
    "化工": {"trend": "稳定", "growth": "3%", "avg_salary": 8000, "outlook": "新材料是增长方向，传统化工饱和"},
    "农林": {"trend": "稳定", "growth": "3%", "salary_median": 6000, "outlook": "智慧农业是新方向，传统农业薪资偏低"},
    "法律": {"trend": "稳定", "growth": "5%", "avg_salary": 9000, "outlook": "合规需求增加，但竞争激烈"},
    "设计": {"trend": "稳定", "growth": "5%", "avg_salary": 8000, "outlook": "AI 设计工具冲击，但创意设计仍有价值"},
}

SPECIAL_ADMISSION = {
    "强基计划": {
        "description": "面向基础学科拔尖学生，39所985高校参与",
        "target": "高考成绩优异 + 校测表现",
        "advantage": "降分录取，本硕博贯通培养",
        "subjects": ["数学", "物理", "化学", "生物", "历史", "哲学", "古文字学"],
        "apply_time": "每年4月",
    },
    "综合评价": {
        "description": "综合高考成绩、学业水平、综合素质评价录取",
        "target": "综合素质优秀的学生",
        "advantage": "降分10-30分录取",
        "schools": ["南方科技大学", "上海科技大学", "昆山杜克大学", "上海纽约大学"],
        "apply_time": "每年3-4月",
    },
    "高校专项计划": {
        "description": "面向农村和贫困地区学生",
        "target": "农村户籍 + 成绩优秀",
        "advantage": "降分录取，最多降60分",
        "apply_time": "每年4月",
    },
    "保送生": {
        "description": "外国语学校推荐保送、奥赛国家集训队保送",
        "target": "外国语学校优秀学生 / 奥赛金牌",
        "advantage": "免高考直接录取",
        "apply_time": "每年11-12月",
    },
    "艺术类招生": {
        "description": "艺术类专业统考/校考 + 高考成绩",
        "target": "有艺术特长的学生",
        "advantage": "文化课要求较低",
        "apply_time": "每年12月-次年3月",
    },
    "体育类招生": {
        "description": "体育统考/单招 + 高考成绩",
        "target": "有体育特长的学生",
        "advantage": "文化课要求较低",
        "apply_time": "每年3-4月",
    },
    "定向招生": {
        "description": "定向培养，毕业回原籍工作",
        "target": "愿意回基层工作的学生",
        "advantage": "降分录取，毕业包分配",
        "fields": ["医学", "师范", "农技"],
        "apply_time": "高考志愿填报时",
    },
    "中外合作办学": {
        "description": "国内高校与国外高校合作办学",
        "target": "家庭经济条件好 + 英语好",
        "advantage": "拿双学位，出国机会多",
        "cost": "学费4-20万/年",
        "apply_time": "高考志愿填报时",
    },
}


def get_industry_trend(industry: str) -> dict:
    return INDUSTRY_TRENDS.get(industry, {"trend": "未知", "growth": "未知", "avg_salary": 0, "outlook": "暂无数据"})


def get_special_admission(name: str) -> dict:
    return SPECIAL_ADMISSION.get(name, {})
