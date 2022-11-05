from pymaya.request_classes.maya_security_base_request import MayaSecurityBaseRequest
from pymaya.utils import Language


class MayaSecurityDataRequest(MayaSecurityBaseRequest):
    end_point = "company/securitydata"
    method = "GET"

    def __init__(self, security_id, lang: Language = Language.ENGLISH):
        super(MayaSecurityDataRequest, self).__init__(lang)
        self.request.params["securityId"] = security_id
        self.request.params["lang"] = int(lang)
