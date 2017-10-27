from nsetools import Nse
from pprint import pprint
from utils import csv_to_dict


class StockReader(object):
    def __init__(self):
    	self.nse = Nse()
    	self.stock_details = csv_to_dict()


    def get_stock_quote(self, stock_code):
    	return self.nse.get_quote(stock_code)


    def get_stock_details(self, stock_code):
    	stock_details = {}
    	stock_dict = self.get_stock_quote(stock_code)
    	stock_details['price'] = stock_dict['lastPrice']
    	stock_details['52_week_high'] = stock_dict['high52']
    	stock_details['52_week_low'] = stock_dict['low52']


    def get_all_codes(self):
    	all_stock_codes = self.nse.get_stock_codes()
    	return all_stock_codes

    def get_stock_details_list(self):
        pprint(self.stock_details)

 

if __name__=="__main__":
	stock = StockReader()
	# all_codes = stock.get_all_codes()
	# pprint(all_codes)
	stock.get_stock_details_list()