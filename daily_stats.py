class DailyStats(object):
	def __init__(self, stats):
		if stats is not None:
			self.open = stats['open']
			self.high = stats['high']
			self.low = stats['low']
			self.volume = stats['volume']
		else:
			self.open = 0
			self.high = 0
			self.low = 0
			self.volume = 0

	def pretty_print(self):
		print ('Daily Stats: {')
		print ('\tOpen: ' + str(self.open))
		print ('\tHigh: ' + str(self.high))
		print ('\tLow: ' + str(self.low))
		print ('\tVolume: ' + str(self.volume))
		print ('}')