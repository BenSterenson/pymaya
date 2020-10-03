from functools import partial
from typing import Dict
from logging import Logger
import traceback
import time

import requests
from cachetools.keys import hashkey
from requests import Session
from cachetools import cachedmethod, LRUCache

from pymaya.request_classes.maya_base_request import MayaBaseRequest
from pymaya.utils import get_logger
from pymaya.exceptions import BadResponseException


class MayaBase:
    def __init__(
        self,
        logger: Logger = None,
        num_of_attempts: int = 1,
        session: Session = Session(),
        verify: bool = True,
        cachesize: int = 128,
    ):
        self.logger = get_logger(self.__class__.__name__) if logger is None else logger
        self.num_of_attempts = num_of_attempts
        self.session = session
        self.verify = verify
        self.cache = LRUCache(maxsize=cachesize)

    def get_response(self, maya_api_request: MayaBaseRequest):
        response = None

        for attempt in range(self.num_of_attempts):
            response = self.session.send(request=maya_api_request.prepare(), verify=self.verify)

            if response.status_code != requests.codes.ok:
                self.logger.info("response error attempt: {}".format(attempt + 1 / self.num_of_attempts))
                self.logger.info("status response code {}, reason {}".format(response.status_code, response.reason))
                self.logger.info("try again in 1 sec...")
                time.sleep(1)

            else:
                return response
        return response

    @cachedmethod(lambda self: self.cache, key=partial(hashkey, "send"))
    def _send_request(self, maya_api_request: MayaBaseRequest) -> Dict:
        try:
            response = self.get_response(maya_api_request=maya_api_request)

            if response.status_code != requests.codes.ok:
                self.logger.error("Error in API call [{}] - {}".format(response.status_code, response.reason))
                raise BadResponseException(
                    status_code=response.status_code,
                    reason=response.reason,
                    url=response.url,
                    method=response.request.method,
                )

            return response.json()

        except Exception as e:
            self.logger.error("Error {}, traceback: {}".format(e, traceback.format_exc()))
            raise
