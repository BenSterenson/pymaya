from pymaya.request_classes.maya_security_base_request import MayaSecurityBaseRequest


class MayaAllSecuritiesRequest(MayaSecurityBaseRequest):
    end_point = 'content/searchentities'
    method = 'GET'

    def __init__(self, lang: int = 1):
        super(MayaSecurityBaseRequest, self).__init__()
        self.request.headers['Content-Type'] = 'application/json'
        self.request.params['lang'] = lang
