import requests
import aiohttp


class Asset:
    def __init__(self, symbol, asynchronous=False):
        self._is_asynchronous = asynchronous
        self._symbol = symbol

    def _refresh(self):
        pass

    def get_price_history(self, range="1d", interval="1m"):
        asset_request = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{self.symbol}?range={range}&interval={interval}"
        )
        asset_request_json = asset_request.json()

    @property
    def symbol(self):
        return self._symbol

    @property
    def exchange_name(self):
        return self._exchange_name

    @property
    def exchange_symbol(self):
        return self._exchange_symbol

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def first_trade_timestamp(self):
        return self._first_trade_timestamp

    @property
    def exchange_timezone(self):
        return self._exchange_timezone

    @property
    def exchange_timezone_name(self):
        return self._exchange_timezone_name

    @property
    def price(self):
        return self._price

    @property
    def day_high(self):
        return self._day_high

    @property
    def day_low(self):
        return self._day_low

    @property
    def fifty_two_week_high(self):
        return self._fifty_two_week_high

    @property
    def fifty_two_week_low(self):
        return self._fifty_two_week_low

    @property
    def volume(self):
        return self._volume
