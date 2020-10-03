from datetime import date

from pymaya.maya import Maya
from pymaya.utils import Language


def main():
    maya = Maya()
    all_securities = maya.get_all_securities(lang=Language.HEBREW)
    print(all_securities)

    print(maya.get_names("739037"))
    print(maya.get_names("5113428"))

    maya.get_details("739037")
    historical_prices = maya.get_price_history(security_id="739037", from_data=date(2017, 12, 31))
    for fund_object in historical_prices:
        print(fund_object)

    maya.get_details("5118393")
    historical_prices = maya.get_price_history(security_id="5118393", from_data=date(2017, 12, 31))
    for fund_object in historical_prices:
        print(fund_object)


if __name__ == "__main__":
    main()

