import requests
import aiohttp

from .price_history import PriceHistory
from .live_price import LivePrice
from .exceptions import PyMarketConnectionError


class Asset:
    def __init__(self, symbol, asynchronous=False):
        self._is_asynchronous = asynchronous
        self._live_price = LivePrice(symbol)
        self._symbol = symbol
        self._refresh()

    def _set_properties_from_json(self, json_payload):
        result = json_payload["chart"]["result"][0]
        indicator_quotes = result["indicators"]["quote"][0]
        meta = result["meta"]
        timestamps = result["timestamp"]
        highs = indicator_quotes["high"]
        lows = indicator_quotes["low"]
        opens = indicator_quotes["open"]
        closes = indicator_quotes["close"]
        self._exchange_symbol = meta["exchangeName"]
        self._exchange_name = meta["fullExchangeName"]
        self._asset_type = meta["instrumentType"]
        self._first_trade_timestamp = meta["firstTradeDate"]
        self._exchange_timezone = meta["timezone"]
        self._exchange_timezone_name = meta["exchangeTimezoneName"]
        self._day_high = meta["regularMarketDayHigh"]
        self._day_low = meta["regularMarketDayLow"]
        self._fifty_two_week_high = meta["fiftyTwoWeekHigh"]
        self._fifty_two_week_low = meta["fiftyTwoWeekLow"]
        self._volume = meta["regularMarketVolume"]
        self._price_history = PriceHistory(timestamps, highs, lows, opens, closes)

    def _refresh(self):
        try:
            asset_request = requests.get(
                f"https://query1.finance.yahoo.com/v8/finance/chart/{self.symbol}",
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                },
            )
        except Exception as e:
            raise PyMarketConnectionError(e)
        asset_request_json = asset_request.json()
        self._set_properties_from_json(asset_request_json)

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
    def live_price(self):
        return self._live_price

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
