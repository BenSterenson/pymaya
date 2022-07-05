from typing import Optional
from datetime import date

from pymaya.request_classes.maya_fund_base_request import MayaFundBaseRequest
from pymaya.utils import Language


class MayaHistoricalRequest(MayaFundBaseRequest):
    end_point = "fund/history"
    method = "POST"

    def __init__(
        self,
        security_id: str,
        from_data: Optional[date],
        to_date: Optional[date],
        page: int = 1,
        period: int = 0,
        lang: Language = Language.ENGLISH,
    ):
        super(MayaHistoricalRequest, self).__init__(lang, data={})
        self.request.headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.request.data["DateFrom"] = from_data.isoformat() if from_data else None
        self.request.data["DateTo"] = to_date.isoformat() if to_date else None
        self.request.data["FundId"] = security_id
        self.request.data["Page"] = page
        self.request.data["Period"] = period
