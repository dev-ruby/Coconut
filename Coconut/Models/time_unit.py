from enum import Enum

__all__ = ["TimeUnit"]


class TimeUnit(Enum):
    MINUTE = ("분", "60분")
    HOUR = ("시간", "24시간")
    DAY = ("일", "30일")
    MONTH = ("달", "12달")

    def __init__(self, kor_name: str, scope: str):
        self.kor_name = kor_name
        self.scope = scope

    @staticmethod
    def from_name(raw: str):
        raw = raw.upper()

        time_unit = {
            "분": TimeUnit.MINUTE,
            "MINUTE": TimeUnit.MINUTE,
            "시": TimeUnit.HOUR,
            "시간": TimeUnit.HOUR,
            "HOUR": TimeUnit.HOUR,
            "일": TimeUnit.DAY,
            "DAY": TimeUnit.DAY,
            "달": TimeUnit.MONTH,
            "월": TimeUnit.MONTH,
            "MONTH": TimeUnit.MONTH,
        }.get(raw)

        return time_unit
