from .models import StudentInput, FamilyCondition, SubjectType
from .engine import ZhangXuefengEngine
from .output import format_result


def main():
    print("=" * 50)
    print("  高考志愿分析（张雪峰框架）")
    print("=" * 50)
    print()

    score = int(input("请输入高考分数："))
    province = input("请输入省份（如：北京）：")
    print("科类：1.理科 2.文科 3.新高考")
    subject_choice = input("请选择科类（1/2/3）：")
    subject = {
        "1": SubjectType.SCIENCE,
        "2": SubjectType.LIBERAL_ARTS,
        "3": SubjectType.NEW_GAOKAO,
    }[subject_choice]
    rank = int(input("请输入位次："))
    print("家庭条件：1.有矿 2.普通 3.困难")
    family_choice = input("请选择家庭条件（1/2/3）：")
    family = {
        "1": FamilyCondition.RICH,
        "2": FamilyCondition.NORMAL,
        "3": FamilyCondition.POOR,
    }[family_choice]

    student = StudentInput(
        score=score,
        province=province,
        subject=subject,
        rank=rank,
        family=family,
    )

    engine = ZhangXuefengEngine()
    result = engine.analyze(student)

    print()
    print(format_result(result))


if __name__ == "__main__":
    main()
