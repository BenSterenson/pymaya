from pymaya.request_classes.maya_base_request import MayaBaseRequest


class MayaMutualFundHistoricalRequest(MayaBaseRequest):
    maya_api_base_url = "https://maya.tase.co.il/api/v1/"
    method = "POST"

    def __init__(self, security_id: str, page: int = 1, page_size: int = 20):
        self._security_id = security_id
        super(MayaMutualFundHistoricalRequest, self).__init__(
            json={"pageSize": page_size, "pageNumber": page}
        )
        self.request.headers["referer"] = "https://maya.tase.co.il/"
        self.request.headers["Content-Type"] = "application/json"
        self.request.headers["Accept"] = "application/json"

    @property
    def end_point(self) -> str:
        return f"funds/mutual/{self._security_id}/history"
