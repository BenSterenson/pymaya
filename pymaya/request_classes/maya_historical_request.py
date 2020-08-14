from datetime import date

from fake_useragent import UserAgent

from pymaya.request_classes.maya_base_request import MayaBaseRequest


class MayaHistoricalRequest(MayaBaseRequest):
    end_point = 'fund/history'
    method = 'POST'

    def __init__(self, fund_id, from_data: date, to_date: date, page: int = 1, period: int = 0):
        super(MayaHistoricalRequest, self).__init__(data={})
        self.request.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.request.headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        self.request.data['DateFrom'] = from_data
        self.request.data['DateTo'] = to_date
        self.request.data['FundId'] = fund_id
        self.request.data['Page'] = page
        self.request.data['Period'] = period
