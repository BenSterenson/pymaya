from datetime import date
from typing import Optional

from pymaya.request_classes.maya_base_request import MayaBaseRequest
from pymaya.utils import FundHistoryPeriod


class MayaMutualFundHistoricalRequest(MayaBaseRequest):
    maya_api_base_url = "https://maya.tase.co.il/api/v1/"
    method = "POST"

    def __init__(
        self,
        security_id: str,
        page: int = 1,
        page_size: int = 30,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
    ):
        self._security_id = security_id
        body = {"pageSize": page_size, "pageNumber": page}
        if from_date is not None or to_date is not None:
            body["period"] = int(FundHistoryPeriod.CUSTOM)
            if from_date is not None:
                body["fromDate"] = from_date.isoformat() + "T00:00:00.000Z"
            if to_date is not None:
                body["toDate"] = to_date.isoformat() + "T00:00:00.000Z"
        else:
            body["period"] = int(FundHistoryPeriod.MONTH)
        super(MayaMutualFundHistoricalRequest, self).__init__(json=body)
        self.request.headers["referer"] = "https://maya.tase.co.il/"
        self.request.headers["Content-Type"] = "application/json"
        self.request.headers["Accept"] = "application/json"

    @property
    def end_point(self) -> str:
        return f"funds/mutual/{self._security_id}/history"
