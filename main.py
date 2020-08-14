from datetime import date
from pymaya.maya import Maya


def main():
    maya = Maya()
    historical_prices = maya.get_price_history(fund_id=5118393, from_data=date(2017, 12, 31))

    for fund_object in historical_prices:
        print(fund_object)


if __name__ == "__main__":
    main()
