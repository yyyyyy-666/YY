from dataclasses import dataclass
from enum import Enum


class FamilyCondition(Enum):
    RICH = "有矿"
    NORMAL = "普通"
    POOR = "困难"


class SubjectType(Enum):
    SCIENCE = "理科"
    LIBERAL_ARTS = "文科"
    NEW_GAOKAO = "新高考"


@dataclass
class StudentInput:
    score: int
    province: str
    subject: SubjectType
    rank: int
    family: FamilyCondition
    city_preference: str = ""


@dataclass
class CityRecommendation:
    city: str
    reason: str


@dataclass
class UniversityRecommendation:
    name: str
    tier: str
    reason: str
    score_range: str


@dataclass
class MajorRecommendation:
    name: str
    employment_rate: float
    salary_median: int
    reason: str
    warning: str = ""
    jobs: str = ""
    industries: str = ""


@dataclass
class AnalysisResult:
    cities: list[CityRecommendation]
    universities: list[UniversityRecommendation]
    majors: list[MajorRecommendation]
    warnings: list[str]
    summary: str
