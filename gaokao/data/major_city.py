import json

# 张雪峰专业-城市匹配（哪些专业在哪些城市最好就业）
MAJOR_CITY_MATCH = {
    "计算机科学与技术": {
        "第一梯队城市": [
            {"city": "北京", "reason": "互联网大厂集中，字节/百度/美团总部", "avg_salary": 18000},
            {"city": "上海", "reason": "互联网+金融科技，拼多多/小红书总部", "avg_salary": 17000},
            {"city": "深圳", "reason": "腾讯总部，硬件+软件生态完善", "avg_salary": 16000},
            {"city": "杭州", "reason": "阿里巴巴总部，电商+互联网氛围", "avg_salary": 15000},
        ],
        "第二梯队城市": [
            {"city": "广州", "reason": "网易/微信总部，生活成本低", "avg_salary": 13000},
            {"city": "成都", "reason": "游戏+互联网，生活品质高", "avg_salary": 11000},
            {"city": "武汉", "reason": "光谷，互联网公司多", "avg_salary": 10000},
            {"city": "南京", "reason": "软件产业发达", "avg_salary": 11000},
        ],
    },
    "人工智能": {
        "第一梯队城市": [
            {"city": "北京", "reason": "AI研究院集中，百度/字节AI lab", "avg_salary": 22000},
            {"city": "上海", "reason": "商汤/旷视分部，AI创业公司多", "avg_salary": 20000},
            {"city": "深圳", "reason": "华为/腾讯AI lab，硬件+AI结合", "avg_salary": 19000},
            {"city": "杭州", "reason": "阿里达摩院，AI+电商", "avg_salary": 18000},
        ],
        "第二梯队城市": [
            {"city": "成都", "reason": "AI创业公司增多", "avg_salary": 14000},
            {"city": "武汉", "reason": "光谷AI产业", "avg_salary": 13000},
            {"city": "西安", "reason": "军工+AI", "avg_salary": 12000},
        ],
    },
    "金融学": {
        "第一梯队城市": [
            {"city": "上海", "reason": "金融中心，券商/基金集中", "avg_salary": 16000},
            {"city": "北京", "reason": "监管机构+银行总部", "avg_salary": 15000},
            {"city": "深圳", "reason": "深交所，私募基金多", "avg_salary": 14000},
            {"city": "香港", "reason": "国际金融中心", "avg_salary": 20000},
        ],
        "第二梯队城市": [
            {"city": "杭州", "reason": "蚂蚁集团，金融科技", "avg_salary": 12000},
            {"city": "广州", "reason": "广发证券总部", "avg_salary": 11000},
            {"city": "成都", "reason": "西南金融中心", "avg_salary": 9000},
        ],
    },
    "临床医学": {
        "第一梯队城市": [
            {"city": "北京", "reason": "协和/北大医学部，顶级医疗资源", "avg_salary": 15000},
            {"city": "上海", "reason": "瑞金/中山医院，医疗水平高", "avg_salary": 14000},
            {"city": "广州", "reason": "南方医科大学附属医院多", "avg_salary": 12000},
        ],
        "第二梯队城市": [
            {"city": "成都", "reason": "华西医院，西南医疗中心", "avg_salary": 10000},
            {"city": "武汉", "reason": "同济/协和医院", "avg_salary": 10000},
            {"city": "长沙", "reason": "湘雅医院", "avg_salary": 9000},
        ],
    },
    "电子信息工程": {
        "第一梯队城市": [
            {"city": "深圳", "reason": "华为/OPPO/vivo总部，硬件生态最完善", "avg_salary": 15000},
            {"city": "上海", "reason": "芯片公司集中，中芯国际总部", "avg_salary": 14000},
            {"city": "北京", "reason": "小米/字节硬件部门", "avg_salary": 13000},
        ],
        "第二梯队城市": [
            {"city": "杭州", "reason": "海康威视总部", "avg_salary": 12000},
            {"city": "东莞", "reason": "制造业中心，硬件供应链", "avg_salary": 10000},
            {"city": "成都", "reason": "电子科大，芯片产业", "avg_salary": 10000},
        ],
    },
    "电气工程": {
        "第一梯队城市": [
            {"city": "北京", "reason": "国家电网总部，电力设计院", "avg_salary": 14000},
            {"city": "上海", "reason": "电力设备公司多", "avg_salary": 13000},
            {"city": "深圳", "reason": "新能源+电力电子", "avg_salary": 12000},
        ],
        "第二梯队城市": [
            {"city": "杭州", "reason": "新能源产业", "avg_salary": 11000},
            {"city": "西安", "reason": "电力设备制造", "avg_salary": 9000},
            {"city": "武汉", "reason": "电力设计院", "avg_salary": 9000},
        ],
    },
    "土木工程": {
        "第一梯队城市": [
            {"city": "北京", "reason": "中建/中铁总部", "avg_salary": 12000},
            {"city": "上海", "reason": "基建项目多", "avg_salary": 11000},
            {"city": "深圳", "reason": "城市建设需求大", "avg_salary": 11000},
        ],
        "第二梯队城市": [
            {"city": "成都", "reason": "西部基建中心", "avg_salary": 9000},
            {"city": "武汉", "reason": "长江大桥等基建项目", "avg_salary": 8500},
            {"city": "重庆", "reason": "山城基建需求", "avg_salary": 8500},
        ],
    },
    "新闻学": {
        "第一梯队城市": [
            {"city": "北京", "reason": "央视/人民日报/新华社总部", "avg_salary": 10000},
            {"city": "上海", "reason": "澎湃/界面新闻，新媒体发达", "avg_salary": 9000},
            {"city": "广州", "reason": "南方报业集团", "avg_salary": 8000},
        ],
        "第二梯队城市": [
            {"city": "成都", "reason": "新媒体产业", "avg_salary": 7000},
            {"city": "杭州", "reason": "MCN机构多", "avg_salary": 7500},
            {"city": "长沙", "reason": "芒果TV，娱乐传媒", "avg_salary": 7000},
        ],
    },
    "法学": {
        "第一梯队城市": [
            {"city": "北京", "reason": "最高法院/最高检察院，红圈律所", "avg_salary": 14000},
            {"city": "上海", "reason": "外所/红圈所分部，涉外法律", "avg_salary": 13000},
            {"city": "深圳", "reason": "涉外法律需求大", "avg_salary": 12000},
        ],
        "第二梯队城市": [
            {"city": "广州", "reason": "珠三角法律需求", "avg_salary": 10000},
            {"city": "成都", "reason": "西南法律中心", "avg_salary": 8000},
            {"city": "武汉", "reason": "华中法律中心", "avg_salary": 8000},
        ],
    },
    "机械工程": {
        "第一梯队城市": [
            {"city": "深圳", "reason": "大疆/比亚迪，智能制造", "avg_salary": 13000},
            {"city": "上海", "reason": "汽车+航空制造", "avg_salary": 12000},
            {"city": "东莞", "reason": "制造业中心", "avg_salary": 10000},
        ],
        "第二梯队城市": [
            {"city": "广州", "reason": "广汽/制造业", "avg_salary": 10000},
            {"city": "苏州", "reason": "精密制造", "avg_salary": 10000},
            {"city": "宁波", "reason": "模具/汽车零部件", "avg_salary": 9000},
        ],
    },
}


def get_major_city_match(major: str) -> dict:
    return MAJOR_CITY_MATCH.get(major, {})
