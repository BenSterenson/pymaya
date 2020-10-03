from datetime import date

from pymaya.request_classes.maya_security_base_request import MayaSecurityBaseRequest
from pymaya.utils import Language


class MayaSecurityHistoricalRequest(MayaSecurityBaseRequest):
    end_point = "security/historyeod"
    method = "POST"

    def __init__(
        self,
        security_id: str,
        from_data: date,
        to_date: date,
        page: int = 1,
        p_type: int = 8,
        total_rec: int = 1,
        lang: Language = Language.ENGLISH,
    ):
        super(MayaSecurityBaseRequest, self).__init__()
        self.request.headers["Content-Type"] = "application/json"
        self.request.json = {
            "dFrom": str(from_data),
            "dTo": str(to_date),
            "oId": str(security_id),
            "pageNum": page,
            "pType": str(p_type),
            "TotalRec": total_rec,
            "lang": str(int(lang)),
        }
