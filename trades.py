import datetime

class Trades(object):
	def __init__(self, trade_history):
		if trade_history is not None:
			self.trades = []
			for trade in trade_history:
				new_trade = Trade(trade)
				self.trades.append(new_trade)
		else:
			self.trades = []

	def pretty_print(self):
		print('Trades: [')
		for trade in self.trades:
			trade.pretty_print()
		print(']')

	def get_sell_count(self):
		count = 0
		for trade in self.trades:
			if 'sell' == trade.get_side():
				count += 1
		return count

	def get_buy_count(self):
		count = 0
		for trade in self.trades:
			if 'buy' == trade.get_side():
				count += 1
		return count


class Trade(object):
	def __init__(self, trade_obj):
		if trade_obj is not None:
			self.time = trade_obj['time']
			self.trade_id = trade_obj['trade_id']
			self.price = trade_obj['price']
			self.side = trade_obj['side']
		else:
			self.time = datetime.datetime.now().isoformat()
			self.trade_id = 'abc'
			self.price = 123
			self.side = 'buy'

	def pretty_print(self):
		to_print = '\t[ Time: ' + str(self.time)
		to_print += ' Trade_Id: ' + str(self.trade_id)
		to_print += ' Price: ' + str(self.price)
		to_print += ' Side: ' + str(self.side) + ' ]'
		print (to_print)

	def get_side(self):
		return self.side