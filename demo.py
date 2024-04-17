from pymarkets import Asset


sp500 = Asset("^GSPC")

sp500.symbol
sp500.exchange_name
sp500.exchange_symbol
sp500.asset_type
sp500.first_trade_timestamp
sp500.exchange_timezone
sp500.exchange_timezone_name
sp500.price
sp500.day_high
sp500.day_low
sp500.fifty_two_week_high
sp500.fifty_two_week_low
sp500.volume
sp500.get_price_history(range="1mo", interval="1d")