from pymaya.request_classes.maya_security_base_request import MayaSecurityBaseRequest
from pymaya.utils import Language


class MayaSecurityDetailsRequest(MayaSecurityBaseRequest):
    end_point = "security/majordata"
    method = "GET"

    def __init__(self, security_id, lang: Language = Language.ENGLISH):
        super(MayaSecurityDetailsRequest, self).__init__(lang)
        self.request.params["secId"] = security_id
        self.request.params["compId"] = security_id[:3]
        self.request.params["lang"] = int(lang)
