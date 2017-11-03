import gdax
from enum import Enum

class GdaxWrapper(object):
	#def __init__(self):

	def getRawOrderBook(pair, order_level=1):
		public_client = gdax.PublicClient()
		order_book = public_client.get_product_order_book(str(pair), level=order_level)
		return order_book

	def getRawTicker(pair):
		public_client = gdax.PublicClient()
		ticker = public_client.get_product_ticker(str(pair))
		return ticker

	def getRawTrades(pair):
		public_client = gdax.PublicClient()
		trades = public_client.get_product_trades(product_id=str(pair))
		return trades

	def getRawHistoricRates(pair):
		public_client = gdax.PublicClient()
		historic_rates = public_client.get_product_historic_rates(str(pair))
		return historic_rates

	def getRaw24hrStats(pair):
		public_client = gdax.PublicClient()
		daily_stats = public_client.get_product_24hr_stats(str(pair))
		return daily_stats

	def getRawCurrencies():
		public_client = gdax.PublicClient()
		currencies = public_client.get_currencies()
		return currencies

	def getCurrentPrice(pair):
		public_client = gdax.PublicClient()
		ticker = public_client.get_product_ticker(str(pair))
		return ticker['price']


class Pair(Enum):
	BTCUSD = 1
	ETHUSD = 2
	LTCUSD = 3
	BTCEUR = 4
	ETHEUR = 5
	LTCEUR = 6
	BTCGBP = 7
	ETHGBP = 8
	LTCGBP = 9

	def __str__(self):
		return self.name[:3] + '-' + self.name[3:]

	def getFiat(self):
		return self.name[3:]

	def getCrypto(self):
		return self.name[:3]