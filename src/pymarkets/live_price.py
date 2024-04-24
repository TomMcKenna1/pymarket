import requests
import functools

from .exceptions import PyMarketConnectionError


@functools.total_ordering
class LivePrice:
    def __init__(self, asset_symbol):
        self._asset_symbol = asset_symbol
        self._value = None

    def _refresh(self):
        try:
            asset_request = requests.get(
                f"https://query1.finance.yahoo.com/v8/finance/chart/{self._asset_symbol}",
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                },
            )
        except Exception as e:
            raise PyMarketConnectionError(e)
        asset_request_json = asset_request.json()
        self._value = asset_request_json["chart"]["result"][0]["meta"][
            "regularMarketPrice"
        ]

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return self.value

    def __eq__(self, value):
        return self.value == value

    def __lt__(self, value):
        return self.value < value

    @property
    def value(self):
        self._refresh()
        return self._value
