class OrderBook(object):
	def __init__(self, order_book):
		self.bids = []
		self.asks = []
		if order_book is not None:
			for bid in order_book['bids']:
				new_bid = BidAskEntry(bid)
				self.bids.append(new_bid)
			for ask in order_book['asks']:
				new_ask = BidAskEntry(ask)
				self.asks.append(new_ask)

	def getBids(self):
		return self.bids

	def getAsks(self):
		return self.asks

	def appendBid(self, bid):
		if type(bid) is BidAskEntry:
			self.bids.append(bid)

	def appendAsk(self, ask):
		if type(bid) is BidAskEntry:
			self.asks.append(ask)

	def pretty_print(self):
		print ('{ ')
		print ('\tAsks: [')
		for bid in self.bids:
			bid.pretty_print()
		print ('\t],')
		print ('\tBids: [')
		for ask in self.asks:
			ask.pretty_print()
		print ('\t]')
		print ('}')


class BidAskEntry(object):
	def __init__(self, entry):
		if entry is not None:
			self.price = entry[0]
			self.size = entry[1]
			self.number_orders = entry[2]
		else:
			self.price = 0
			self.size = 0.0
			self.number_orders = 0

	def pretty_print(self):
		print ('\t\t[ Price: ' + str(self.price) + ', Size: ' + str(self.size) + ', Number of Orders: ' + str(self.number_orders) + ' ]')