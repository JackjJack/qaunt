import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Returns the most recent transactions by U.S. Representatives
routes = {
    'house' : "https://api.quiverquant.com/beta/live/housetrading",
    # Returns the most recent transactions by members of U.S. Congress
    'congress' : "https://api.quiverquant.com/beta/live/congresstrading",
    # Returns all of the stock transactions by U.S. Senators involving the given ticker
    'senate' : "https://api.quiverquant.com/beta/live/senatetrading",
    # Returns the 500 most recently announced contracts across all companies
    'contracts' : "https://api.quiverquant.com/beta/live/govcontractsall",
    # Returns last quarter's government contract amounts for all companies
    'quarterly_contracts' : "https://api.quiverquant.com/beta/live/govcontracts",
    # Returns the most recent lobbying spending instances across all companies.
    'corp_lobbying' : "https://api.quiverquant.com/beta/live/lobbying",
    # Returns yesterday's off-exchange activity across all companies.
    'off_exchange' : "https://api.quiverquant.com/beta/live/offexchange",
    # Returns all of the stock transactions by members of U.S. Congress involving the given ticker
    'congress_ticker' : "https://api.quiverquant.com/beta/historical/congresstrading/{ticker}"
          }


class GetData():

    def __init__(self):
        self.data = []
        self.sector = None
        self.url = None

    def get(self, sector):
        self.sector = sector
        self.url = routes[sector]
        headers = {'accept': 'application/json',
                   'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
                   'Authorization': 'api.quiverwuant.com'}
        r = requests.get(self.url, headers=headers)
        self.data.append(json.loads(r.content))
        return self.data
        
               
    
x = GetData()


house_info = x.get('house')
congress_info = x.get('congress')
senate_info = x.get('senate')
contracts = x.get('contracts')
quarterly_contracts = x.get('quarterly_contracts')
corp_lobbying = x.get('corp_lobbying')
off_exchange = x.get('off_exchange')
congress_ticker = x.get('congress_ticker')

all_data_raw = house_info + congress_info + senate_info + contracts + quarterly_contracts + corp_lobbying
all_data = list(filter(None, all_data_raw))

def count_tickers(data):
    clean_data = []
    dict_count = 0
    other_count  = 0
    data_types = []
    ticker_list = []
    
    
    for i in data:
        for j in i:
            clean_data.append(j)
    
    for i in clean_data:
        if isinstance(i, dict):
            dict_count += 1
        else:
            other_count += 1
    
    if other_count > 0:
        raise Exception('All of the data is not in a dictionary!',
                        'The total dictionary count is: ' + str(dict_count),
                        'The other data types are: ' + str(data_types))
    else:
        for i in clean_data:
            ticker_list.append(i['Ticker'])
        
        ticker_count = {ticker: 0 for ticker in ticker_list}    
        for i in ticker_list:
            if i in ticker_list:
                ticker_count[i] += 1
    #pprint(ticker_count)
    #print('The toal dictionary count is: ' + str(dict_count))
    #print('The other data type count is: ' + str(other_count))
    return ticker_count
         
organized_data = count_tickers(all_data)

def find_top_ten_traded(data):
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    top_ten = (dict(list(sorted_data.items())[:10]))
    return top_ten
    
bar_sample = find_top_ten_traded(organized_data)

keys = bar_sample.keys()
values = bar_sample.values()

plt.bar(keys, values)
plt.show()
    