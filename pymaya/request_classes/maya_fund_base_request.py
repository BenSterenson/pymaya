from abc import abstractmethod

from pymaya.request_classes.maya_base_request import MayaBaseRequest
from pymaya.utils import Language


class MayaFundBaseRequest(MayaBaseRequest):
    maya_api_base_url = "https://mayaapi.tase.co.il/api/"

    def __init__(self, lang, *args, **kwargs):
        super(MayaFundBaseRequest, self).__init__(*args, **kwargs)
        self.request.headers["X-Maya-With"] = "allow"
        self.request.headers["Accept-Language"] = "en-US" if lang == Language.ENGLISH else "he-IL"

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass
