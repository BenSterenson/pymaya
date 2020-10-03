from pymaya.request_classes.maya_fund_base_request import MayaFundBaseRequest
from pymaya.utils import Language


class MayaFundDetailsRequest(MayaFundBaseRequest):
    end_point = "fund/details"
    method = "GET"

    def __init__(self, security_id, lang: Language = Language.ENGLISH):
        super(MayaFundDetailsRequest, self).__init__(lang)
        self.request.params["fundId"] = security_id
