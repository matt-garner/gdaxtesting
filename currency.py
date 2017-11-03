class Currencies(object):
	def __init__(self, currencies_list):
		if currencies_list is not None:
			self.currencies = []
			for currency in currencies_list:
				new_currency = Currency(currency)
				self.currencies.append(new_currency)
		else:
			self.currencies = []

	def pretty_print(self):
		print ('Currencies: [')
		for currency in self.currencies:
			currency.pretty_print()
		print (']')

class Currency(object):
	def __init__(self, currency):
		if currency is not None:
			self.id = currency['id']
			self.name = currency['name']
			self.min_size = currency['min_size']
		else:
			self.id = 'USD'
			self.name = 'United States Dollar'
			self.min_size = '0.01000'

	def pretty_print(self):
		to_print = '\t{ ID: ' + str(self.id)
		to_print += ' Name: ' + str(self.name)
		to_print += ' Min_Size: ' + str(self.min_size) + ' }'
		print (to_print)
