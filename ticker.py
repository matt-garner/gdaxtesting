class Ticker(object):
	def __init__(self, ticker):
		if ticker is not None:
			self.price = float(ticker['price'])
			self.bid = float(ticker['bid'])
			self.ask = float(ticker['ask'])
			self.volume = float(ticker['volume'])
		else:
			self.price = 0
			self.bid = 0
			self.ask = 0
			self.volume = 0

	def pretty_print(self):
		print('{')
		print('\tPrice: ' + str(self.price))
		print('\tBid: ' + str(self.bid))
		print('\tAsk: ' + str(self.ask))
		print('\tVolume: ' + str(self.volume))
		print('}')