class HistoricRates(object):
	def __init__(self, historical_rates):
		if historical_rates is not None:
			self.historical_rates = []
			for rate_itr in historical_rates:
				new_rate = Rate(rate_itr)
				self.historical_rates.append(new_rate)
		else:
			self.historical_rates = []

	def pretty_print(self):
		print ('Historic Rates: [')
		for rate in self.historical_rates:
			rate.pretty_print()
		print (']')

class Rate(object):
	def __init__(self, historic_rate):
		if historic_rate is not None:
			self.time = historic_rate[0]
			self.low = historic_rate[1]
			self.high = historic_rate[2]
			self.open = historic_rate[3]
			self.close = historic_rate[4]
			self.volume = historic_rate[5]

	def pretty_print(self):
		to_print = '\t[ Time: ' + str(self.time)
		to_print += ' Low: ' + str(self.low)
		to_print += ' High: ' + str(self.high)
		to_print += ' Open: ' + str(self.open)
		to_print += ' Close: ' + str(self.close)
		to_print += ' Volume: ' + str(self.volume) + ' ]'
		print (to_print)