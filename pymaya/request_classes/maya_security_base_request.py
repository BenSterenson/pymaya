from abc import abstractmethod

from pymaya.request_classes.maya_base_request import MayaBaseRequest


class MayaSecurityBaseRequest(MayaBaseRequest):
    maya_api_base_url = "https://api.tase.co.il/api/"

    def __init__(self, *args, **kwargs):
        super(MayaSecurityBaseRequest, self).__init__(*args, **kwargs)

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass
