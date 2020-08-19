# pymaya intract with 
- https://maya.tase.co.il/
- https://api.tase.co.il/

pip install pymaya
example:

```
from datetime import date

from pymaya.maya import Maya


def main():
    maya = Maya()
    all_securities = maya.get_all_securities()
    print(all_securities)

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

```
