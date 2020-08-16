from pymaya.request_classes.maya_security_base_request import MayaSecurityBaseRequest


class MayaSecurityDetailsRequest(MayaSecurityBaseRequest):
    end_point = 'security/majordata'
    method = 'GET'

    def __init__(self, security_id, lang: int = 1):
        super(MayaSecurityDetailsRequest, self).__init__()
        self.request.params['secId'] = security_id
        self.request.params['compId'] = security_id[:3]
        self.request.params['lang'] = lang
