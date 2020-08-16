from abc import abstractmethod

from pymaya.request_classes.maya_base_request import MayaBaseRequest


class MayaFundBaseRequest(MayaBaseRequest):
    maya_api_base_url = 'https://mayaapi.tase.co.il/api/'

    def __init__(self, *args, **kwargs):
        super(MayaFundBaseRequest, self).__init__(*args, **kwargs)
        self.request.headers['X-Maya-With'] = "allow"

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass
