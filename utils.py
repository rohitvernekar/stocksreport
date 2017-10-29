
import csv

def csv_to_dict():
    '''

    This code converts csv to dict

    '''
    dict_details = {}
    reader = csv.DictReader(open('stock_list.csv', 'rb'), delimiter='|')
    for line in reader:
        keys = line.keys()
        vals = line.values()
        dict_details[vals[0]] = {keys[1]: vals[1], keys[2]: vals[2], keys[3]: vals[3]}
    return dict_details