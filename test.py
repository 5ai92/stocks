#author : bhargav sai dama
# Just inserted one more line
from googlefinance import getQuotes
from yahoo_finance import Share
import timeit
from threads import Repeat
import threading
import Queue
import multiprocessing

class Stock:
    stockcount = 0
    
    def __init__(self, symbol, c_name, sector, industry):
        self.symbol = symbol
        self.c_name = c_name
        self.sector = sector
        self.industry = industry
        Stock.stockcount += 1
    
    def display_count(self):
        return "Total count of stocks %s" %(Stock.stockcount)
    
    def display_stock(self):
        return "Company : %s , symbol : %s" %(self.c_name, self.symbol)
    
    def current(self):
        open_price = float(Share(self.symbol).get_open())
        curr_price = float(getQuotes(self.symbol)[0]['LastTradeWithCurrency'])
        change_price = round((curr_price-open_price),2)
        change_percent =round(((change_price/open_price) * 100), 2)
        return open_price, curr_price, change_price, change_percent
    
    def historical_volume(self, from_date, to_date):
        historical = Share(self.symbol).get_historical(from_date, to_date)
        return historical
        
    def fundementals(self):
        marketcap = (Share(self.symbol).get_market_cap())
        bookvalue = Share(self.symbol).get_book_value()
        dividend = Share(self.symbol).get_dividend_share()
        dividend_paydate = Share(self.symbol).get_dividend_pay_date()
        dividend_yield = Share(self.symbol).get_dividend_yield()
        
        return (marketcap, bookvalue, dividend, dividend_paydate, dividend_yield)


stock1 = Stock('aapl', 'Apple Inc.Ltd', 'technology', 'Manufacturing')
stock2 = Stock('suzy', 'Suzlon India Ltd', 'Energy', 'Manufacturing')


def main():
    
    # print threading.active_count()
    # print threading.enumerate()
    # print threading.current_thread()
   
    start_time = timeit.default_timer()
    
    print stock1.display_stock()
    print stock1.current()
    print stock1.fundementals()
    #print(stock1.historical_volume('2014-04-25', '2014-04-29'))
    print "total stocks listed now are %s" %(Stock.stockcount)
    print (timeit.default_timer() - start_time)
    
    # start = timeit.default_timer()
    
    # p1 = multiprocessing.Process(target = stock1.display_stock)
    
    # p1.start()
    # p1.join()
    
    # print (timeit.default_timer() - start)

if __name__ == '__main__':
    main()

        
        
