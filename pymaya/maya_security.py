from functools import partial
from typing import List, Dict
from datetime import date

from cachetools import cachedmethod
from cachetools.keys import hashkey

from pymaya.maya_base import MayaBase
from pymaya.request_classes.maya_all_securities_request import MayaAllSecuritiesRequest
from pymaya.request_classes.maya_security_details_request import MayaSecurityDetailsRequest
from pymaya.request_classes.maya_security_request import MayaSecurityHistoricalRequest
from pymaya.utils import streamify


class MayaSecurity(MayaBase):

    @cachedmethod(lambda self: self.cache, key=partial(hashkey, 'all'))
    def get_all_securities(self, lang: int = 1):
        return self._send_request(MayaAllSecuritiesRequest(lang))

    def get_details(self, security_id: str):
        return self._send_request(MayaSecurityDetailsRequest(security_id))

    def get_price_history_chunk(self, security_id: str, from_data: date, to_date: date, page: int) -> Dict:
        return self._send_request(MayaSecurityHistoricalRequest(security_id, from_data, to_date, page))

    @streamify
    def get_price_history(self, security_id: str, from_data: date, to_date: date = date.today(), page: int = 1) -> List[Dict]:
        data = self.get_price_history_chunk(security_id, from_data, to_date, page)
        return data.get("Items", [])
