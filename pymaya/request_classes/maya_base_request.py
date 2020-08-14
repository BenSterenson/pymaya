from abc import ABC, abstractmethod

from urllib.parse import urljoin

import requests


class MayaBaseRequest(ABC):
    MAYA_API_BASE_URL = 'https://mayaapi.tase.co.il/api/'

    def __init__(self, *args, **kwargs):
        self.request = requests.Request(self.method, **kwargs)
        self.request.headers['Cache-Control'] = 'no-cache'
        self.request.headers['X-Maya-With'] = "allow"

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass

    def _get_url(self) -> str:
        return urljoin(self.MAYA_API_BASE_URL, self.end_point)

    def prepare(self) -> requests.PreparedRequest:
        self.request.url = self._get_url()
        return self.request.prepare()
