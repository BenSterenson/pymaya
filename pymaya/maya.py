from logging import Logger
from typing import List, Dict
from datetime import date

from requests import Session

from pymaya.maya_funds import MayaFunds
from pymaya.maya_security import MayaSecurity
from pymaya.utils import Language


class Maya:
    def __init__(
        self,
        logger: Logger = None,
        num_of_attempts: int = 1,
        session: Session = Session(),
        verify: bool = True,
        cachesize: int = 128,
    ):

        self.maya_securities = MayaSecurity(
            logger=logger, num_of_attempts=num_of_attempts, session=session, verify=verify, cachesize=cachesize
        )

        self.maya_funds = MayaFunds(
            logger=logger, num_of_attempts=num_of_attempts, session=session, verify=verify, cachesize=cachesize
        )

        self.mapped_securities = {}
        self.map_securities()

    def get_all_securities(self, lang: Language = Language.ENGLISH):
        return self.maya_securities.get_all_securities(lang)

    def map_securities(self):
        all_securities = self.get_all_securities()
        for security in all_securities:
            if security.get("Id") in self.mapped_securities:
                self.mapped_securities[security.get("Id")].add(security.get("Type"))
            else:
                self.mapped_securities[security.get("Id")] = {(security.get("Type"))}

    def get_maya_class(self, security_id: str):
        if MayaFunds.TYPE in self.mapped_securities.get(security_id):
            return self.maya_funds
        else:
            return self.maya_securities

    def get_details(self, security_id: str, lang: Language = Language.ENGLISH):
        maya_class = self.get_maya_class(security_id)
        return maya_class.get_details(security_id, lang)

    def get_names(self, security_id: str):
        maya_class = self.get_maya_class(security_id)
        english_details = maya_class.get_details(security_id, lang=Language.ENGLISH)
        hebrew_details = maya_class.get_details(security_id, lang=Language.HEBREW)
        return maya_class.get_names(english_details, hebrew_details)

    def get_price_history_chunk(
        self, security_id: str, from_data: date, to_date: date, page: int, lang: Language = Language.ENGLISH
    ) -> Dict:
        maya_class = self.get_maya_class(security_id)
        return maya_class.get_price_history_chunk(
            security_id, from_data=from_data, to_date=to_date, page=page, lang=lang
        )

    def get_price_history(
        self,
        security_id: str,
        from_data: date,
        to_date: date = date.today(),
        page: int = 1,
        lang: Language = Language.ENGLISH,
    ):
        maya_class = self.get_maya_class(security_id)
        return maya_class.get_price_history(security_id, from_data=from_data, to_date=to_date, page=page, lang=lang)
