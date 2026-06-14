CITY_DATA = {
    "北京市": {"tier": 1, "avg_salary": 12000, "cost_level": "高", "job_market": "极好", "highlights": ["互联网", "金融", "科技", "文化"]},
    "上海市": {"tier": 1, "avg_salary": 11500, "cost_level": "高", "job_market": "极好", "highlights": ["金融", "贸易", "互联网", "汽车"]},
    "广州市": {"tier": 1, "avg_salary": 10000, "cost_level": "中高", "job_market": "好", "highlights": ["贸易", "制造", "互联网", "电商"]},
    "深圳市": {"tier": 1, "avg_salary": 11000, "cost_level": "高", "job_market": "极好", "highlights": ["科技", "金融", "互联网", "硬件"]},
    "杭州市": {"tier": 2, "avg_salary": 10500, "cost_level": "中高", "job_market": "极好", "highlights": ["互联网", "电商", "金融", "游戏"]},
    "南京市": {"tier": 2, "avg_salary": 9500, "cost_level": "中", "job_market": "好", "highlights": ["软件", "电子", "教育", "化工"]},
    "成都市": {"tier": 2, "avg_salary": 8500, "cost_level": "中", "job_market": "好", "highlights": ["互联网", "游戏", "电子", "食品"]},
    "武汉市": {"tier": 2, "avg_salary": 8500, "cost_level": "中", "job_market": "好", "highlights": ["光电子", "汽车", "教育", "生物"]},
    "西安市": {"tier": 2, "avg_salary": 7500, "cost_level": "中低", "job_market": "中", "highlights": ["军工", "航天", "教育", "旅游"]},
    "长沙市": {"tier": 2, "avg_salary": 8000, "cost_level": "中", "job_market": "好", "highlights": ["制造", "文娱", "教育", "食品"]},
    "南昌市": {"tier": 3, "avg_salary": 7000, "cost_level": "中低", "job_market": "中", "highlights": ["制造", "航空", "电子", "食品"]},
    "合肥市": {"tier": 2, "avg_salary": 8500, "cost_level": "中", "job_market": "好", "highlights": ["科技", "制造", "新能源", "半导体"]},
    "苏州市": {"tier": 2, "avg_salary": 9500, "cost_level": "中", "job_market": "好", "highlights": ["制造", "电子", "生物医药", "纳米"]},
    "天津市": {"tier": 2, "avg_salary": 8500, "cost_level": "中", "job_market": "中", "highlights": ["制造", "化工", "航空", "港口"]},
    "重庆市": {"tier": 2, "avg_salary": 7500, "cost_level": "中低", "job_market": "中", "highlights": ["汽车", "电子", "制造", "互联网"]},
    "大连市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "中", "highlights": ["软件", "港口", "制造", "旅游"]},
    "青岛市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "中", "highlights": ["家电", "啤酒", "港口", "旅游"]},
    "厦门市": {"tier": 3, "avg_salary": 8000, "cost_level": "中高", "job_market": "中", "highlights": ["电子", "旅游", "贸易", "软件"]},
    "郑州市": {"tier": 3, "avg_salary": 7000, "cost_level": "中低", "job_market": "中", "highlights": ["交通", "制造", "食品", "电商"]},
    "济南市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "中", "highlights": ["制造", "软件", "教育", "医疗"]},
    "福州市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "中", "highlights": ["电子", "纺织", "食品", "数字"]},
    "昆明市": {"tier": 3, "avg_salary": 6500, "cost_level": "中低", "job_market": "中低", "highlights": ["旅游", "生物", "烟草", "花卉"]},
    "贵阳市": {"tier": 3, "avg_salary": 6500, "cost_level": "低", "job_market": "中低", "highlights": ["大数据", "旅游", "白酒", "材料"]},
    "南宁市": {"tier": 3, "avg_salary": 6500, "cost_level": "低", "job_market": "中低", "highlights": ["制造", "糖业", "旅游", "东盟贸易"]},
    "太原市": {"tier": 3, "avg_salary": 6500, "cost_level": "低", "job_market": "中低", "highlights": ["煤炭", "钢铁", "化工", "重工"]},
    "石家庄市": {"tier": 3, "avg_salary": 6500, "cost_level": "低", "job_market": "中", "highlights": ["制药", "纺织", "化工", "教育"]},
    "哈尔滨市": {"tier": 3, "avg_salary": 6000, "cost_level": "低", "job_market": "中低", "highlights": ["重工", "食品", "航天", "教育"]},
    "长春市": {"tier": 3, "avg_salary": 6000, "cost_level": "低", "job_market": "中低", "highlights": ["汽车", "轨道", "食品", "教育"]},
    "沈阳市": {"tier": 3, "avg_salary": 6500, "cost_level": "低", "job_market": "中", "highlights": ["重工", "航空", "机器人", "装备"]},
    "兰州市": {"tier": 3, "avg_salary": 6000, "cost_level": "低", "job_market": "中低", "highlights": ["石化", "核技术", "教育", "旅游"]},
    "呼和浩特市": {"tier": 3, "avg_salary": 6000, "cost_level": "低", "job_market": "中低", "highlights": ["乳业", "能源", "旅游"]},
    "乌鲁木齐市": {"tier": 3, "avg_salary": 6000, "cost_level": "低", "job_market": "中低", "highlights": ["能源", "矿产", "农业", "旅游"]},
    "银川市": {"tier": 3, "avg_salary": 5500, "cost_level": "低", "job_market": "低", "highlights": ["能源", "农业", "旅游"]},
    "西宁市": {"tier": 3, "avg_salary": 5500, "cost_level": "低", "job_market": "低", "highlights": ["能源", "矿产", "旅游"]},
    "拉萨市": {"tier": 3, "avg_salary": 5500, "cost_level": "低", "job_market": "低", "highlights": ["旅游", "能源", "文化"]},
    "保定市": {"tier": 4, "avg_salary": 5500, "cost_level": "低", "job_market": "中低", "highlights": ["汽车", "制造", "新能源"]},
    "洛阳市": {"tier": 4, "avg_salary": 5500, "cost_level": "低", "job_market": "中低", "highlights": ["重工", "装备", "旅游"]},
    "徐州市": {"tier": 4, "avg_salary": 6000, "cost_level": "低", "job_market": "中", "highlights": ["重工", "制造", "教育"]},
    "扬州市": {"tier": 4, "avg_salary": 6500, "cost_level": "中低", "job_market": "中", "highlights": ["制造", "旅游", "食品"]},
    "无锡市": {"tier": 2, "avg_salary": 9000, "cost_level": "中", "job_market": "好", "highlights": ["制造", "物联网", "半导体", "影视"]},
    "常州市": {"tier": 4, "avg_salary": 7000, "cost_level": "中低", "job_market": "中", "highlights": ["制造", "新能源", "装备"]},
    "宁波市": {"tier": 3, "avg_salary": 8500, "cost_level": "中", "job_market": "好", "highlights": ["港口", "制造", "外贸", "服装"]},
    "温州市": {"tier": 4, "avg_salary": 7000, "cost_level": "中低", "job_market": "中", "highlights": ["制造", "鞋服", "电器"]},
    "东莞市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "好", "highlights": ["电子", "制造", "外贸"]},
    "佛山市": {"tier": 3, "avg_salary": 7500, "cost_level": "中", "job_market": "好", "highlights": ["家电", "陶瓷", "制造"]},
    "珠海市": {"tier": 3, "avg_salary": 8000, "cost_level": "中", "job_market": "中", "highlights": ["电子", "航空", "医药"]},
    "厦门市": {"tier": 3, "avg_salary": 8000, "cost_level": "中高", "job_market": "中", "highlights": ["电子", "旅游", "贸易"]},
    "烟台市": {"tier": 4, "avg_salary": 6500, "cost_level": "中低", "job_market": "中", "highlights": ["制造", "食品", "黄金"]},
    "潍坊市": {"tier": 4, "avg_salary": 6000, "cost_level": "低", "job_market": "中", "highlights": ["农业", "制造", "化工"]},
    "赣州市": {"tier": 4, "avg_salary": 5500, "cost_level": "低", "job_market": "中低", "highlights": ["稀土", "制造", "农业"]},
    "九江市": {"tier": 4, "avg_salary": 5500, "cost_level": "低", "job_market": "中低", "highlights": ["石化", "纺织", "旅游"]},
}


def get_city_info(city: str) -> dict:
    if city in CITY_DATA:
        return CITY_DATA[city]
    for key in CITY_DATA:
        if city in key or key.startswith(city):
            return CITY_DATA[key]
    return {"tier": 4, "avg_salary": 6000, "cost_level": "中低", "job_market": "中", "highlights": []}


def get_cities_by_tier(tier: int) -> list:
    return [city for city, info in CITY_DATA.items() if info["tier"] == tier]
