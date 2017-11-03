import order_book
import ticker
import trades
import historic_rates
import daily_stats
import currency
import user
from gdax_wrapper import Pair
from gdax_wrapper import GdaxWrapper


#############################################################################################################
# Main Class, main loop will eventually be implemented here													#
# each section below is a test of a different module, uncomment to test the feature							#
#############################################################################################################


#############################################################################################################
#Testing Order Book
#new_order_book = order_book.OrderBook(GdaxWrapper.getRawOrderBook(Pair.BTCUSD, 1))
#new_order_book.pretty_print()

#############################################################################################################
#Testing Ticker
#new_ticker = ticker.Ticker(GdaxWrapper.getRawTicker(Pair.BTCUSD))
#new_ticker.pretty_print()

#############################################################################################################
#Testing Trades
#new_trades = trades.Trades(GdaxWrapper.getRawTrades(Pair.BTCUSD))
#new_trades.pretty_print()
#print ('Buys: ' + str(new_trades.get_buy_count()))
#print ('Sells: ' + str(new_trades.get_sell_count()))

#############################################################################################################
#Testing Historic Rates
#new_historic_rates = historic_rates.HistoricRates(GdaxWrapper.getRawHistoricRates(Pair.BTCUSD))
#new_historic_rates.pretty_print()

#############################################################################################################
#Testing Daily Stats
#new_daily_stats = daily_stats.DailyStats(GdaxWrapper.getRaw24hrStats(Pair.BTCUSD))
#new_daily_stats.pretty_print()

#############################################################################################################
#Testing Currencies
#new_currencies = currency.Currencies(GdaxWrapper.getRawCurrencies())
#new_currencies.pretty_print()

#############################################################################################################
#Testing Transactions and user class
#t1 = { 'ts': '112345', 'pair': Pair.BTCUSD, 'price': '400.10', 'amount': '1.1'}
#t2 = { 'ts': '11234125', 'pair': Pair.BTCUSD, 'price': '700.10', 'amount': '1.1'}
#t3 = { 'ts': '11234515', 'pair': Pair.BTCUSD, 'price': '900.10', 'amount': '1.1'}
#transactions = []
#transactions.append(t1)
#transactions.append(t2)
#transactions.append(t3)
#new_user = user.User(Pair.BTCUSD, transactions)
#new_user.printLongPortfolio()

#############################################################################################################
# Next steps, begin using authenticated client 																#
# add configuration file for user's api keys																#
# and then build a bridge between the user's transaction history in coinbase/gdax and the user class here	#
#############################################################################################################