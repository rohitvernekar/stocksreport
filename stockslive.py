from nsetools import Nse
from pprint import pprint
from utils import csv_to_dict


class StockReader(object):
    def __init__(self):
        self.nse = Nse()
        self.stock_details = csv_to_dict()

    def get_stock_quote(self, stock_code):
        """
        This gives all the details of the stock
        """
    	return self.nse.get_quote(stock_code)


    def get_stock_details(self, stock_code):
        stock_dict = self.get_stock_quote(stock_code)
        self.stock_details[stock_code]['price'] = stock_dict['lastPrice']
        self.stock_details[stock_code]['52_week_high'] = stock_dict['high52']
        self.stock_details[stock_code]['52_week_low'] = stock_dict['low52']


    def get_all_codes(self):
    	all_stock_codes = self.nse.get_stock_codes()
    	return all_stock_codes

    def get_stock_details_list(self):
        for stock_code in self.stock_details.keys():
            self.get_stock_details(stock_code)
        pprint(self.stock_details)

    def total(self):
        total_bought_price = 0
        total_price = 0
        total_high = 0
        total_low = 0
        for value in self.stock_details.values():

            total_bought_price += float(value[' brought_price']) * int(value[' quantity '])
            total_price += float(value['price']) * int(value[' quantity '])
            total_high += float(value['52_week_high']) * int(value[' quantity '])
            total_low += float(value['52_week_low']) * int(value[' quantity '])

        print "Total brought price %s " % total_bought_price
        print "Todays total price %s" % total_price
        print "Total high price %s" % total_high
        print "Total low  price %s" % total_low


if __name__=="__main__":
    stock = StockReader()
    # all_codes = stock.get_all_codes()
    # pprint(all_codes)
    stock.get_stock_details_list()
    stock.total()