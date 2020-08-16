from pymaya.request_classes.maya_fund_base_request import MayaFundBaseRequest


class MayaFundDetailsRequest(MayaFundBaseRequest):
    end_point = 'fund/details'
    method = 'GET'

    def __init__(self, security_id):
        super(MayaFundDetailsRequest, self).__init__()
        self.request.params['fundId'] = security_id
