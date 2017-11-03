import gdax_wrapper

class User(object):
	def __init__(self, pair, transaction_history):
		if transaction_history is not None:
			self.transactions = []
			self.pair = pair
			for transaction in transaction_history:
				self.transactions.append(Transaction(transaction))
		else:
			self.transactions = []

	def getPortfolioValue(self):
		curr_price = gdax_wrapper.GdaxWrapper.getCurrentPrice(self.pair)
		running_value = 0
		for transaction in self.transactions:
			running_value += transaction.getCurrentValue(curr_price)
		return running_value

	def getPortfolioOriginalValue(self):
		running_value = 0
		for transaction in self.transactions:
			running_value += transaction.getOriginalValue()
		return running_value

	def getPortfolioOverallChange(self):
		curr_price = gdax_wrapper.GdaxWrapper.getCurrentPrice(self.pair)
		original_value = self.getPortfolioOriginalValue()
		current_value = self.getPortfolioValue()
		return current_value - original_value

	def printPortfolioOverallChange(self, curr_price):
		change = self.getPortfolioOverallChange()
		print ('The change to your portfolio has been: ' + str(change) + ' ' + self.pair.getFiat())

	def printLongPortfolio(self):
		print ('Your transaction history and changes are as follows:')
		#for each transaction we want atomic details:
		curr_price = gdax_wrapper.GdaxWrapper.getCurrentPrice(self.pair)
		for transaction in self.transactions:
			transaction.printChangeInTransaction(curr_price)


class Transaction(object):
	def __init__(self, details):
		self.time = details['ts']
		self.pair = details['pair']
		self.price = details['price']
		self.amount = details['amount']

	def calculateValueChange(self, curr_price):
		return self.getCurrentValue(curr_price) - self.getOriginalValue()

	def calculatePercentChange(self, curr_price):
		increase = self.getCurrentValue(curr_price) - self.getOriginalValue()
		increase_dec = increase / self.getOriginalValue()
		return increase_dec*100

	def getOriginalValue(self):
		original_value = float(self.price) * float(self.amount)
		return original_value

	def getCurrentValue(self, curr_price):
		current_value = float(curr_price) * float(self.amount)
		return current_value

	def printChangeInTransaction(self, curr_price):
		to_print = 'Your transaction of ' + str("{0:.2f}".format(float(self.amount))) + ' ' + self.pair.getCrypto()
		to_print += ' originally cost ' + str("{0:.2f}".format(float(self.getOriginalValue())))
		to_print += ' and is now worth ' + str("{0:.2f}".format(float(self.getCurrentValue(curr_price))))
		to_print += ' for an increase of ' + str("{0:.2f}".format(float(self.calculateValueChange(curr_price)))) + ' ' + self.pair.getFiat()
		to_print += ' or ' + str("{0:.2f}".format(float(self.calculatePercentChange(curr_price)))) + '%'
		print (to_print)
