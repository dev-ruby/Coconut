from enum import Enum

__all__ = ["CoinType"]


class CoinType(Enum):
    BITCOIN = ("BTC", "KRW-BTC", "비트코인", "BITCOIN")
    RIPPLE = ("XRP", "KRW-XRP", "리플", "RIPPLE")
    ETHEREUM = ("ETH", "KRW-ETH", "이더리움", "ETHEREUM")
    DOGECOIN = ("DOGE", "KRW-DOGE", "도지코인", "DOGECOIN")

    def __init__(self, abbreviation: str, code: str, kor_name: str, eng_name: str):
        self.abbreviation = abbreviation
        self.code = code
        self.kor_name = kor_name
        self.eng_name = eng_name

    @staticmethod
    def from_name(raw: str):
        raw = raw.upper()

        coin_type = {
            "비트": CoinType.BITCOIN,
            "비트코인": CoinType.BITCOIN,
            "BITCOIN": CoinType.BITCOIN,
            "BTC": CoinType.BITCOIN,
            "KRW-BTC": CoinType.BITCOIN,
            "이더": CoinType.ETHEREUM,
            "이더리움": CoinType.ETHEREUM,
            "ETH": CoinType.ETHEREUM,
            "KRW-ETH": CoinType.ETHEREUM,
            "ETHEREUM": CoinType.ETHEREUM,
            "리플": CoinType.RIPPLE,
            "XRP": CoinType.RIPPLE,
            "KRW-XRP": CoinType.RIPPLE,
            "RIPPLE": CoinType.RIPPLE,
            "도지": CoinType.DOGECOIN,
            "도지코인": CoinType.DOGECOIN,
            "DOGE": CoinType.DOGECOIN,
            "KRW-DOGE": CoinType.DOGECOIN,
            "DOGECOIN": CoinType.DOGECOIN,
        }.get(raw)

        return coin_type
