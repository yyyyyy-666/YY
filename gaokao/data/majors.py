MAJORS = [
    # ==================== 计算机/软件类 ====================
    {"name": "计算机科学与技术", "jobs": "软件工程师, 前端工程师, 后端工程师", "industries": "互联网, 金融, 游戏", "category": "工科", "employment_rate": 0.95, "salary_median": 12000, "ai_impact": "中等", "warning": "", "recommendation": "强烈推荐", "match_types": ["理工类", "综合类"]},
    {"name": "软件工程", "jobs": "软件工程师, 全栈工程师, DevOps工程师", "industries": "互联网, 金融, 企业服务", "category": "工科", "employment_rate": 0.96, "salary_median": 13000, "ai_impact": "中等", "warning": "", "recommendation": "强烈推荐", "match_types": ["理工类", "综合类"]},
    {"name": "人工智能", "jobs": "AI工程师, 算法工程师, 机器学习工程师", "industries": "互联网, 自动驾驶, 医疗AI", "category": "工科", "employment_rate": 0.93, "salary_median": 15000, "ai_impact": "低", "warning": "需要读研", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "数据科学与大数据技术", "jobs": "数据分析师, 数据工程师, 大数据开发", "industries": "互联网, 金融, 电商", "category": "工科", "employment_rate": 0.94, "salary_median": 13000, "ai_impact": "低", "warning": "", "recommendation": "强烈推荐", "match_types": ["理工类", "综合类"]},
    {"name": "信息安全", "jobs": "安全工程师, 渗透测试, 安全运维", "industries": "互联网, 金融, 政府", "category": "工科", "employment_rate": 0.94, "salary_median": 11000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "网络空间安全", "jobs": "安全工程师, 安全研究员, 安全架构师", "industries": "互联网, 政府, 军工", "category": "工科", "employment_rate": 0.93, "salary_median": 12000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "物联网工程", "jobs": "嵌入式工程师, IoT开发, 硬件工程师", "industries": "智能家居, 工业互联网, 车联网", "category": "工科", "employment_rate": 0.91, "salary_median": 10000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "智能科学与技术", "jobs": "AI工程师, 算法工程师, 智能系统开发", "industries": "互联网, 机器人, 自动驾驶", "category": "工科", "employment_rate": 0.92, "salary_median": 12000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "区块链工程", "category": "工科", "employment_rate": 0.88, "salary_median": 11000, "ai_impact": "低", "warning": "行业波动大", "recommendation": "一般", "match_types": ["理工类", "综合类"]},
    {"name": "数字媒体技术", "jobs": "游戏开发, 多媒体工程师, VR/AR开发", "industries": "游戏, 影视, 广告", "category": "工科", "employment_rate": 0.90, "salary_median": 9500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "网络工程", "jobs": "网络工程师, 运维工程师, 网络架构师", "industries": "运营商, 互联网, 企业IT", "category": "工科", "employment_rate": 0.92, "salary_median": 10000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 电子/通信类 ====================
    {"name": "电子信息工程", "jobs": "硬件工程师, 嵌入式工程师, 射频工程师", "industries": "通信, 芯片, 消费电子", "category": "工科", "employment_rate": 0.93, "salary_median": 10500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "通信工程", "jobs": "通信工程师, 射频工程师, 协议工程师", "industries": "运营商, 通信设备, 5G", "category": "工科", "employment_rate": 0.92, "salary_median": 10000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "微电子科学与工程", "jobs": "芯片设计工程师, 验证工程师, 工艺工程师", "industries": "半导体, 芯片, 集成电路", "category": "工科", "employment_rate": 0.91, "salary_median": 11000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "光电信息科学与工程", "jobs": "光学工程师, 光通信工程师, 激光工程师", "industries": "光通信, 激光, 显示", "category": "工科", "employment_rate": 0.90, "salary_median": 9500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "信息工程", "jobs": "信号处理工程师, 通信工程师, 算法工程师", "industries": "通信, 互联网, 军工", "category": "工科", "employment_rate": 0.91, "salary_median": 10000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "集成电路设计与集成系统", "jobs": "芯片设计, 验证工程师, 后端工程师", "industries": "半导体, 芯片, EDA", "category": "工科", "employment_rate": 0.92, "salary_median": 12000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 电气/自动化类 ====================
    {"name": "电气工程及其自动化", "jobs": "电气工程师, 电力系统工程师, 自动化工程师", "industries": "电力, 新能源, 制造业", "category": "工科", "employment_rate": 0.93, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "自动化", "jobs": "自动化工程师, PLC工程师, 控制系统工程师", "industries": "制造业, 电力, 机器人", "category": "工科", "employment_rate": 0.92, "salary_median": 10000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "机器人工程", "jobs": "机器人工程师, 自动化工程师, 算法工程师", "industries": "机器人, 制造业, 物流", "category": "工科", "employment_rate": 0.91, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "智能制造工程", "jobs": "智能制造工程师, 自动化工程师, MES工程师", "industries": "制造业, 汽车, 电子", "category": "工科", "employment_rate": 0.91, "salary_median": 9500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 机械/汽车类 ====================
    {"name": "机械工程", "jobs": "机械工程师, 结构工程师, 工艺工程师", "industries": "制造业, 汽车, 航空", "category": "工科", "employment_rate": 0.90, "salary_median": 9000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "机械设计制造及其自动化", "jobs": "机械工程师, 设计工程师, 制造工程师", "industries": "制造业, 汽车, 重工", "category": "工科", "employment_rate": 0.91, "salary_median": 9000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "车辆工程", "jobs": "汽车工程师, 底盘工程师, 动力总成工程师", "industries": "汽车, 新能源车, 零部件", "category": "工科", "employment_rate": 0.90, "salary_median": 9000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 能源/新能源类 ====================
    {"name": "新能源科学与工程", "jobs": "新能源工程师, 光伏工程师, 储能工程师", "industries": "光伏, 风电, 储能", "category": "工科", "employment_rate": 0.92, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "新能源汽车工程", "jobs": "新能源汽车工程师, 电池工程师, 电驱工程师", "industries": "新能源车, 电池, 充电桩", "category": "工科", "employment_rate": 0.93, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "储能科学与工程", "jobs": "储能工程师, 电池工程师, 系统工程师", "industries": "储能, 电池, 电力", "category": "工科", "employment_rate": 0.91, "salary_median": 9500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 土木/建筑类 ====================
    {"name": "土木工程", "jobs": "土木工程师, 结构工程师, 项目经理", "industries": "建筑, 房地产, 基建", "category": "工科", "employment_rate": 0.88, "salary_median": 8500, "ai_impact": "低", "warning": "行业下行", "recommendation": "慎选", "match_types": ["理工类", "综合类"]},
    {"name": "建筑学", "jobs": "建筑师, 城市规划师, 室内设计师", "industries": "建筑设计, 房地产, 城市规划", "category": "工科", "employment_rate": 0.85, "salary_median": 8000, "ai_impact": "中等", "warning": "行业下行", "recommendation": "慎选", "match_types": ["理工类", "综合类"]},
    {"name": "城乡规划", "jobs": "城市规划师, 景观设计师, 规划咨询", "industries": "规划设计, 政府, 房地产", "category": "工科", "employment_rate": 0.84, "salary_median": 7500, "ai_impact": "中等", "warning": "行业下行", "recommendation": "慎选", "match_types": ["理工类", "综合类"]},
    {"name": "给排水科学与工程", "jobs": "给排水工程师, 水处理工程师, 市政工程师", "industries": "市政, 环保, 建筑", "category": "工科", "employment_rate": 0.87, "salary_median": 8000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["理工类", "综合类"]},
    # ==================== 航空/航天类 ====================
    {"name": "航空航天工程", "jobs": "航空工程师, 航天工程师, 飞行器设计师", "industries": "航空, 航天, 军工", "category": "工科", "employment_rate": 0.92, "salary_median": 11000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "飞行器设计与工程", "jobs": "飞行器设计师, 结构工程师, 气动工程师", "industries": "航空, 航天, 无人机", "category": "工科", "employment_rate": 0.91, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    # ==================== 医学类 ====================
    {"name": "临床医学", "jobs": "医生, 住院医师, 主治医师", "industries": "医院, 诊所, 医疗研究", "category": "医学", "employment_rate": 0.90, "salary_median": 8000, "ai_impact": "低", "warning": "学制长(5+3+3)", "recommendation": "有条件推荐", "match_types": ["医药类", "综合类"]},
    {"name": "口腔医学", "jobs": "口腔医生, 正畸医生, 种植医生", "industries": "口腔医院, 诊所", "category": "医学", "employment_rate": 0.92, "salary_median": 10000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["医药类", "综合类"]},
    {"name": "麻醉学", "jobs": "麻醉医生, 疼痛科医生", "industries": "医院", "category": "医学", "employment_rate": 0.93, "salary_median": 9000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["医药类", "综合类"]},
    {"name": "医学影像学", "jobs": "影像医生, 超声医生, 放射科医生", "industries": "医院, 影像中心", "category": "医学", "employment_rate": 0.91, "salary_median": 8500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["医药类", "综合类"]},
    {"name": "药学", "jobs": "药剂师, 药物研发, 药品注册", "industries": "药企, 医院, CRO", "category": "医学", "employment_rate": 0.88, "salary_median": 7500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["医药类", "综合类"]},
    {"name": "中药学", "jobs": "中药师, 中药研发, 质量管理", "industries": "中药企业, 医院", "category": "医学", "employment_rate": 0.86, "salary_median": 7000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["医药类", "综合类"]},
    {"name": "护理学", "jobs": "护士, 护理管理, 专科护士", "industries": "医院, 诊所, 养老", "category": "医学", "employment_rate": 0.95, "salary_median": 6000, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["医药类", "综合类"]},
    {"name": "预防医学", "jobs": "公卫医师, 流行病学家, 健康管理", "industries": "疾控, 医院, 健康管理", "category": "医学", "employment_rate": 0.88, "salary_median": 7000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["医药类", "综合类"]},
    {"name": "中医学", "jobs": "中医师, 针灸师, 推拿师", "industries": "中医院, 诊所", "category": "医学", "employment_rate": 0.85, "salary_median": 6500, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["医药类", "综合类"]},
    {"name": "法医学", "jobs": "法医, 司法鉴定人", "industries": "公安, 司法鉴定", "category": "医学", "employment_rate": 0.89, "salary_median": 7500, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["医药类", "综合类"]},
    # ==================== 财经类 ====================
    {"name": "金融学", "jobs": "银行柜员, 投资分析师, 风控经理", "industries": "银行, 证券, 基金", "category": "文科", "employment_rate": 0.88, "salary_median": 9000, "ai_impact": "高", "warning": "需要名校+实习", "recommendation": "有条件推荐", "match_types": ["财经类", "综合类"]},
    {"name": "金融工程", "jobs": "量化分析师, 风控工程师, 金融产品经理", "industries": "证券, 基金, 银行", "category": "文科", "employment_rate": 0.87, "salary_median": 9500, "ai_impact": "高", "warning": "需要名校", "recommendation": "有条件推荐", "match_types": ["财经类", "综合类"]},
    {"name": "会计学", "jobs": "会计师, 审计师, 财务经理", "industries": "会计事务所, 企业财务, 银行", "category": "文科", "employment_rate": 0.85, "salary_median": 7000, "ai_impact": "高", "warning": "AI替代风险高", "recommendation": "慎选", "match_types": ["财经类", "综合类"]},
    {"name": "审计学", "jobs": "审计师, 内审经理, 合规经理", "industries": "会计事务所, 企业内审", "category": "文科", "employment_rate": 0.86, "salary_median": 7500, "ai_impact": "高", "warning": "AI替代风险", "recommendation": "慎选", "match_types": ["财经类", "综合类"]},
    {"name": "财务管理", "jobs": "财务经理, 会计, 财务分析师", "industries": "企业财务, 银行, 证券", "category": "文科", "employment_rate": 0.85, "salary_median": 7000, "ai_impact": "高", "warning": "AI替代风险", "recommendation": "慎选", "match_types": ["财经类", "综合类"]},
    {"name": "经济学", "jobs": "经济分析师, 政策研究员, 咨询顾问", "industries": "政府, 研究机构, 咨询", "category": "文科", "employment_rate": 0.84, "salary_median": 7500, "ai_impact": "中等", "warning": "就业面窄", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "国际经济与贸易", "jobs": "外贸专员, 报关员, 国际商务", "industries": "外贸, 物流, 电商", "category": "文科", "employment_rate": 0.82, "salary_median": 7000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "电子商务", "jobs": "电商运营, 客服, 推广专员", "industries": "电商, 零售", "category": "文科", "employment_rate": 0.85, "salary_median": 7000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "市场营销", "jobs": "销售代表, 市场推广, 客户经理", "industries": "各行业通用", "category": "文科", "employment_rate": 0.82, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "工商管理", "jobs": "管理培训生, 项目经理, 运营经理", "industries": "各行业通用", "category": "文科", "employment_rate": 0.83, "salary_median": 7000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "人力资源管理", "jobs": "HR专员, 招聘经理, 薪酬经理", "industries": "各行业通用", "category": "文科", "employment_rate": 0.84, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    # ==================== 法学类 ====================
    {"name": "法学", "jobs": "律师, 法务, 法官", "industries": "律师事务所, 企业法务, 法院", "category": "文科", "employment_rate": 0.80, "salary_median": 7500, "ai_impact": "中等", "warning": "需过法考", "recommendation": "有条件推荐", "match_types": ["政法类", "综合类", "师范类"]},
    {"name": "社会工作", "jobs": "社工, 社区工作者, 公益项目管理", "industries": "社工机构, 社区, 公益", "category": "文科", "employment_rate": 0.78, "salary_median": 5500, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["政法类", "综合类"]},
    {"name": "政治学与行政学", "category": "文科", "employment_rate": 0.79, "salary_median": 6000, "ai_impact": "低", "warning": "就业面窄", "recommendation": "慎选", "match_types": ["政法类", "综合类"]},
    # ==================== 文学/语言类 ====================
    {"name": "汉语言文学", "jobs": "编辑, 文案, 教师", "industries": "出版, 教育, 媒体", "category": "文科", "employment_rate": 0.78, "salary_median": 5500, "ai_impact": "中等", "warning": "就业面窄", "recommendation": "慎选", "match_types": ["综合类", "师范类"]},
    {"name": "英语", "jobs": "翻译, 英语教师, 外贸专员", "industries": "教育, 外贸, 翻译", "category": "文科", "employment_rate": 0.76, "salary_median": 5500, "ai_impact": "高", "warning": "AI翻译冲击", "recommendation": "慎选", "match_types": ["综合类", "师范类", "语言类"]},
    {"name": "日语", "jobs": "日语翻译, 日企员工, 日语教师", "industries": "日企, 外贸, 教育", "category": "文科", "employment_rate": 0.75, "salary_median": 5500, "ai_impact": "高", "warning": "AI翻译冲击", "recommendation": "慎选", "match_types": ["综合类", "语言类"]},
    {"name": "法语", "jobs": "法语翻译, 外贸专员, 法语教师", "industries": "外贸, 翻译, 教育", "category": "文科", "employment_rate": 0.78, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["综合类", "语言类"]},
    {"name": "德语", "jobs": "德语翻译, 德企员工, 德语教师", "industries": "德企, 外贸, 教育", "category": "文科", "employment_rate": 0.77, "salary_median": 6000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["综合类", "语言类"]},
    {"name": "西班牙语", "jobs": "西语翻译, 外贸专员, 西语教师", "industries": "外贸, 翻译, 教育", "category": "文科", "employment_rate": 0.78, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["综合类", "语言类"]},
    {"name": "翻译", "jobs": "笔译, 口译, 本地化专员", "industries": "翻译公司, 外企, 互联网", "category": "文科", "employment_rate": 0.74, "salary_median": 5500, "ai_impact": "高", "warning": "AI翻译冲击大", "recommendation": "慎选", "match_types": ["综合类", "语言类"]},
    # ==================== 新闻/传播类 ====================
    {"name": "新闻学", "jobs": "记者, 编辑, 新媒体运营", "industries": "媒体, 互联网, 公关", "category": "文科", "employment_rate": 0.79, "salary_median": 5800, "ai_impact": "高", "warning": "80%毕业生转行", "recommendation": "慎选", "match_types": ["综合类", "师范类"]},
    {"name": "广告学", "jobs": "广告策划, 创意总监, 媒介经理", "industries": "广告公司, 互联网, 品牌", "category": "文科", "employment_rate": 0.80, "salary_median": 6000, "ai_impact": "高", "warning": "", "recommendation": "慎选", "match_types": ["综合类"]},
    {"name": "传播学", "jobs": "公关专员, 品牌传播, 内容运营", "industries": "公关, 互联网, 媒体", "category": "文科", "employment_rate": 0.79, "salary_median": 5800, "ai_impact": "高", "warning": "", "recommendation": "慎选", "match_types": ["综合类"]},
    {"name": "网络与新媒体", "jobs": "新媒体运营, 内容策划, 短视频运营", "industries": "互联网, MCN, 品牌", "category": "文科", "employment_rate": 0.82, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["综合类"]},
    # ==================== 教育类 ====================
    {"name": "教育学", "jobs": "教师, 教育咨询, 课程设计", "industries": "学校, 培训机构", "category": "文科", "employment_rate": 0.85, "salary_median": 6000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["师范类", "综合类"]},
    {"name": "学前教育", "jobs": "幼师, 早教老师, 园长", "industries": "幼儿园, 早教中心", "category": "文科", "employment_rate": 0.90, "salary_median": 5000, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["师范类", "综合类"]},
    {"name": "小学教育", "jobs": "小学教师, 教育管理", "industries": "学校, 培训机构", "category": "文科", "employment_rate": 0.88, "salary_median": 5500, "ai_impact": "低", "warning": "", "recommendation": "保底", "match_types": ["师范类", "综合类"]},
    {"name": "特殊教育", "jobs": "特教老师, 康复师", "industries": "特教学校, 康复中心", "category": "文科", "employment_rate": 0.87, "salary_median": 5000, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["师范类", "综合类"]},
    # ==================== 理学类 ====================
    {"name": "数学与应用数学", "jobs": "数据分析师, 精算师, 教师", "industries": "金融, 教育, 互联网", "category": "理科", "employment_rate": 0.85, "salary_median": 8000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["综合类", "师范类"]},
    {"name": "统计学", "jobs": "数据分析师, 统计师, 精算师", "industries": "金融, 互联网, 政府", "category": "理科", "employment_rate": 0.88, "salary_median": 9000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["综合类"]},
    {"name": "物理学", "jobs": "研究员, 教师, 工程师", "industries": "科研, 教育, 半导体", "category": "理科", "employment_rate": 0.82, "salary_median": 7000, "ai_impact": "低", "warning": "就业面窄", "recommendation": "一般", "match_types": ["综合类", "师范类"]},
    {"name": "化学", "jobs": "化学工程师, 研发工程师, 教师", "industries": "化工, 制药, 教育", "category": "理科", "employment_rate": 0.80, "salary_median": 6500, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["综合类", "师范类"]},
    {"name": "生物科学", "jobs": "研究员, 实验员, 教师", "industries": "科研, 制药, 教育", "category": "理科", "employment_rate": 0.75, "salary_median": 5500, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["综合类", "师范类"]},
    {"name": "地理科学", "category": "理科", "employment_rate": 0.83, "salary_median": 6000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["综合类", "师范类"]},
    # ==================== 天坑专业 ====================
    {"name": "生物工程", "jobs": "生物工程师, 研发工程师, 质量管理", "industries": "制药, 食品, 生物技术", "category": "理科", "employment_rate": 0.72, "salary_median": 5500, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["理工类", "综合类"]},
    {"name": "化学工程与工艺", "jobs": "化工工程师, 工艺工程师, 研发工程师", "industries": "化工, 石油, 制药", "category": "理科", "employment_rate": 0.75, "salary_median": 6000, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["理工类", "综合类"]},
    {"name": "环境工程", "jobs": "环保工程师, 环评工程师, 水处理工程师", "industries": "环保, 水务, 政府", "category": "理科", "employment_rate": 0.70, "salary_median": 5200, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["理工类", "综合类"]},
    {"name": "材料科学与工程", "jobs": "材料工程师, 研发工程师, 质量工程师", "industries": "材料, 制造, 半导体", "category": "理科", "employment_rate": 0.73, "salary_median": 5800, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["理工类", "综合类"]},
    {"name": "环境科学", "jobs": "环保工程师, 环评工程师, 科研人员", "industries": "环保, 政府, 科研", "category": "理科", "employment_rate": 0.71, "salary_median": 5300, "ai_impact": "低", "warning": "天坑预警:没读博士别碰", "recommendation": "天坑", "match_types": ["理工类", "综合类"]},
    # ==================== 农林类 ====================
    {"name": "农学", "jobs": "农艺师, 育种师, 农业技术员", "industries": "农业, 种业, 农化", "category": "理科", "employment_rate": 0.82, "salary_median": 5500, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["农林类", "综合类"]},
    {"name": "林学", "jobs": "林业工程师, 园林设计师, 生态工程师", "industries": "林业, 园林, 环保", "category": "理科", "employment_rate": 0.80, "salary_median": 5500, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["农林类", "综合类"]},
    {"name": "动物医学", "jobs": "兽医, 动物保健, 宠物医生", "industries": "宠物医院, 畜牧, 制药", "category": "理科", "employment_rate": 0.85, "salary_median": 6000, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["农林类", "综合类"]},
    {"name": "园艺", "jobs": "园艺师, 园林设计师, 农业技术员", "industries": "园林, 农业, 花卉", "category": "理科", "employment_rate": 0.82, "salary_median": 5500, "ai_impact": "低", "warning": "", "recommendation": "保底", "match_types": ["农林类", "综合类"]},
    # ==================== 艺术类 ====================
    {"name": "视觉传达设计", "jobs": "平面设计师, UI设计师, 品牌设计师", "industries": "设计, 互联网, 广告", "category": "艺术", "employment_rate": 0.85, "salary_median": 7000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["艺术类", "综合类"]},
    {"name": "环境设计", "jobs": "室内设计师, 景观设计师, 展览设计师", "industries": "设计, 建筑, 展览", "category": "艺术", "employment_rate": 0.82, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["艺术类", "综合类"]},
    {"name": "产品设计", "jobs": "产品设计师, 工业设计师, UX设计师", "industries": "制造, 互联网, 设计", "category": "艺术", "employment_rate": 0.83, "salary_median": 7000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["艺术类", "综合类"]},
    {"name": "动画", "jobs": "动画师, 游戏美术, 特效师", "industries": "游戏, 影视, 动画", "category": "艺术", "employment_rate": 0.80, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["艺术类", "综合类"]},
    # ==================== 专科专业 ====================
    {"name": "电子信息工程技术", "jobs": "电子工程师, 维修工程师, 测试工程师", "industries": "电子, 制造, 通信", "category": "专科", "employment_rate": 0.95, "salary_median": 7000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "计算机应用技术", "jobs": "程序员, 运维工程师, 技术支持", "industries": "互联网, 企业IT", "category": "专科", "employment_rate": 0.94, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "软件技术", "jobs": "程序员, 测试工程师, 运维工程师", "industries": "互联网, 企业IT", "category": "专科", "employment_rate": 0.94, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "机电一体化技术", "jobs": "机电工程师, 维修工程师, 自动化技术员", "industries": "制造业, 自动化", "category": "专科", "employment_rate": 0.93, "salary_median": 6000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "护理", "jobs": "护士, 护理员, 健康管理师", "industries": "医院, 养老, 诊所", "category": "专科", "employment_rate": 0.96, "salary_median": 5500, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["医药类", "综合类"]},
    {"name": "学前教育", "category": "专科", "employment_rate": 0.95, "salary_median": 4500, "ai_impact": "低", "warning": "薪资偏低", "recommendation": "保底", "match_types": ["师范类", "综合类"]},
    {"name": "大数据与会计", "jobs": "会计, 财务助理, 数据录入", "industries": "企业财务, 会计事务所", "category": "专科", "employment_rate": 0.90, "salary_median": 5500, "ai_impact": "高", "warning": "AI替代风险", "recommendation": "慎选", "match_types": ["财经类", "综合类"]},
    {"name": "建筑工程技术", "jobs": "施工员, 预算员, 监理员", "industries": "建筑, 房地产", "category": "专科", "employment_rate": 0.88, "salary_median": 5500, "ai_impact": "低", "warning": "行业下行", "recommendation": "慎选", "match_types": ["理工类", "综合类"]},
    {"name": "新能源汽车技术", "jobs": "新能源汽车维修, 电池技术员, 充电桩运维", "industries": "新能源车, 充电桩", "category": "专科", "employment_rate": 0.94, "salary_median": 6500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "工业机器人技术", "jobs": "机器人操作, 维修技术员, 编程员", "industries": "制造业, 自动化", "category": "专科", "employment_rate": 0.93, "salary_median": 6500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "物联网应用技术", "jobs": "IoT技术员, 嵌入式开发, 系统集成", "industries": "智能家居, 工业互联网", "category": "专科", "employment_rate": 0.92, "salary_median": 6000, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "大数据技术", "jobs": "数据分析师, 大数据运维, ETL工程师", "industries": "互联网, 金融", "category": "专科", "employment_rate": 0.93, "salary_median": 6500, "ai_impact": "中等", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "人工智能技术应用", "jobs": "AI应用开发, 数据标注, 模型部署", "industries": "互联网, AI公司", "category": "专科", "employment_rate": 0.92, "salary_median": 6500, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "电气自动化技术", "jobs": "电气技术员, PLC编程, 维修电工", "industries": "制造业, 电力", "category": "专科", "employment_rate": 0.93, "salary_median": 6000, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "数控技术", "jobs": "数控操作, 编程员, 维修技术员", "industries": "制造业, 模具", "category": "专科", "employment_rate": 0.92, "salary_median": 5800, "ai_impact": "低", "warning": "", "recommendation": "推荐", "match_types": ["理工类", "综合类"]},
    {"name": "汽车检测与维修技术", "jobs": "汽车维修, 检测技师, 售后服务", "industries": "汽车, 4S店", "category": "专科", "employment_rate": 0.91, "salary_median": 5500, "ai_impact": "低", "warning": "", "recommendation": "一般", "match_types": ["理工类", "综合类"]},
    {"name": "电子商务", "category": "专科", "employment_rate": 0.90, "salary_median": 5500, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "市场营销", "category": "专科", "employment_rate": 0.88, "salary_median": 5000, "ai_impact": "中等", "warning": "", "recommendation": "一般", "match_types": ["财经类", "综合类"]},
    {"name": "酒店管理与数字化运营", "jobs": "酒店管理, 前台管理, 餐饮管理", "industries": "酒店, 旅游", "category": "专科", "employment_rate": 0.87, "salary_median": 4800, "ai_impact": "低", "warning": "", "recommendation": "保底", "match_types": ["综合类"]},
    {"name": "旅游管理", "jobs": "导游, 旅游策划, 景区管理", "industries": "旅游, 酒店", "category": "专科", "employment_rate": 0.86, "salary_median": 4800, "ai_impact": "低", "warning": "", "recommendation": "保底", "match_types": ["综合类"]},
]


def get_dangerous_majors():
    return [m for m in MAJORS if "天坑" in (m.get("warning") or "")]


def get_majors_by_employment(min_rate=0.8):
    return [m for m in MAJORS if m["employment_rate"] >= min_rate]


def get_majors_for_school(school_type, is_vocational=False):
    if is_vocational:
        pool = [m for m in MAJORS if m["category"] == "专科"]
    else:
        pool = [m for m in MAJORS if m["category"] != "专科"]
    
    matched = [m for m in pool if school_type in m.get("match_types", [])]
    if not matched:
        matched = pool
    
    matched = [m for m in matched if "天坑" not in (m.get("warning") or "")]
    matched.sort(key=lambda m: m["salary_median"], reverse=True)
    return matched[:5]


BATCH_LINES = {"一本线": 509, "二本线": 440, "专科线": 200}
