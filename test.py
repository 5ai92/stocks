#author : bhargav sai dama
from googlefinance import getQuotes
from yahoo_finance import Share

class Stock:
    stockcount = 0
    
    def __init__(self, symbol, c_name, sector, industry):
        self.symbol = symbol
        self.c_name = c_name
        self.sector = sector
        self.industry = industry
        Stock.stockcount += 1
    
    def display_count(self):
        print "Total count of stocks %s" %(Stock.stockcount)
    
    def display_stock(self):
        print "Company : %s , symbol : %s" %(self.c_name, self.symbol)
    
    def current(self):
        return getQuotes(self.symbol)[0]['LastTradeWithCurrency']
    
    def today(self):
        return Share(self.symbol).get_open()
        


stock1 = Stock('aapl', 'Apple Inc.Ltd', 'technology', 'Manufacturing')
stock2 = Stock('suzy', 'Suzlon India Ltd', 'Energy', 'Manufacturing')

stock1.current()
stock2.display_stock()

print "total stocks listed now are %s" %(Stock.stockcount)

        
        