from abc import ABC, abstractmethod

from urllib.parse import urljoin

from fake_useragent import UserAgent
import requests


class MayaBaseRequest(ABC):
    def __init__(self, *args, **kwargs):
        self.request = requests.Request(self.method, **kwargs)
        self.request.headers["Cache-Control"] = "no-cache"
        self.request.headers["User-Agent"] = UserAgent(verify_ssl=False).chrome

    @property
    @abstractmethod
    def maya_api_base_url(self):
        pass

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass

    def _get_url(self) -> str:
        return urljoin(self.maya_api_base_url, self.end_point)

    def prepare(self) -> requests.PreparedRequest:
        self.request.url = self._get_url()
        return self.request.prepare()
