from typing import List, Dict
from datetime import date

from pymaya.maya_base import MayaBase
from pymaya.request_classes.maya_fund_details_request import MayaFundDetailsRequest
from pymaya.request_classes.maya_historical_request import MayaHistoricalRequest
from pymaya.utils import streamify


class MayaFunds(MayaBase):
    TYPE = 4

    def get_details(self, security_id: str):
        return self._send_request(MayaFundDetailsRequest(security_id))

    def get_price_history_chunk(self, security_id: str, from_data: date, to_date: date, page: int) -> Dict:
        return self._send_request(MayaHistoricalRequest(security_id, from_data, to_date, page))

    @streamify
    def get_price_history(self, security_id: str, from_data: date, to_date: date = date.today(), page: int = 1) -> List[Dict]:
        data = self.get_price_history_chunk(security_id, from_data, to_date, page)
        return data.get("Table", [])
