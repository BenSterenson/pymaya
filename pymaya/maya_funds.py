from typing import List, Dict, Any, Optional, Union
from datetime import date, datetime

from pymaya.maya_base import MayaBase
from pymaya.request_classes.maya_fund_details_request import MayaFundDetailsRequest
from pymaya.request_classes.maya_mutual_fund_historical_request import MayaMutualFundHistoricalRequest
from pymaya.utils import streamify, Language


def _to_date(d: Union[date, datetime, None]) -> Optional[date]:
    if d is None:
        return None
    return d.date() if isinstance(d, datetime) else d


class MayaFunds(MayaBase):
    TYPE = 4

    @staticmethod
    def get_names(english_details: Dict[str, Any], hebrew_details: Dict[str, Any]):
        return {
            "english_short_name": english_details.get("FundLongName", ""),
            "english_long_name": english_details.get("FundLongName", ""),
            "hebrew_short_name": hebrew_details.get("FundShortName", ""),
            "hebrew_long_name": hebrew_details.get("FundLongName", ""),
        }

    def get_details(self, security_id: str, lang: Language = Language.ENGLISH):
        return self._send_request(MayaFundDetailsRequest(security_id, lang))

    def get_price_history_chunk(
        self, security_id: str, from_date: date, to_date: date, page: int, lang: Language = Language.ENGLISH
    ) -> List[Dict]:
        return self._send_request(
            MayaMutualFundHistoricalRequest(
                security_id,
                page=page,
                from_date=_to_date(from_date),
                to_date=_to_date(to_date),
            )
        )

    @streamify
    def get_price_history(
        self,
        security_id: str,
        from_date: date,
        to_date: date = date.today(),
        page: int = 1,
        lang: Language = Language.ENGLISH,
    ) -> List[Dict]:
        return self.get_price_history_chunk(security_id, from_date, to_date, page, lang)
