from functools import partial
from typing import List, Dict, Any
from datetime import date

from cachetools import cachedmethod
from cachetools.keys import hashkey

from pymaya.maya_base import MayaBase
from pymaya.request_classes.maya_all_securities_request import MayaAllSecuritiesRequest
from pymaya.request_classes.maya_security_data_request import MayaSecurityDataRequest
from pymaya.request_classes.maya_security_request import MayaSecurityHistoricalRequest
from pymaya.utils import streamify, Language


class MayaSecurity(MayaBase):
    @cachedmethod(lambda self: self.cache, key=partial(hashkey, "all"))
    def get_all_securities(self, lang: Language = Language.ENGLISH):
        return self._send_request(MayaAllSecuritiesRequest(lang))

    @staticmethod
    def get_names(english_details: Dict[str, Any], hebrew_details: Dict[str, Any]):
        return {
            "english_short_name": english_details.get('Name'),
            "english_long_name": english_details.get('LongName') or english_details.get('SecurityLongName'),
            "hebrew_short_name": hebrew_details.get("Name"),
            "hebrew_long_name": hebrew_details.get("LongName") or hebrew_details.get('SecurityLongName'),
        }

    def get_details(self, security_id: str, lang: Language = Language.ENGLISH):
        return self._send_request(MayaSecurityDataRequest(security_id, lang=lang))

    def get_price_history_chunk(
        self, security_id: str, from_data: date, to_date: date, page: int, lang: Language = Language.ENGLISH
    ) -> Dict:
        return self._send_request(MayaSecurityHistoricalRequest(security_id, from_data, to_date, page, lang=lang))

    @streamify
    def get_price_history(
        self,
        security_id: str,
        from_data: date,
        to_date: date = date.today(),
        page: int = 1,
        lang: Language = Language.ENGLISH,
    ) -> List[Dict]:

        if not to_date:
            to_date = date.today()

        data = self.get_price_history_chunk(security_id, from_data, to_date, page, lang)
        return data.get("Items", [])
