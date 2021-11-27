import json
import requests

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

cache = []

class GetData():

    def __init__(self):
        self.data = []
        self.sector = None
        self.url = None

    def get(self, sector):
        global cache
        self.sector = sector
        self.url = routes[sector]
        headers = {'accept': 'application/json',
                   'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
                   'Authorization': 'Token a786b7e71b07abce63986c770094c20f9809c12b'}
        r = requests.get(self.url, headers=headers)
        result = json.loads(r.content)
        #print(type(result))
        if result:
            self.data.append(result)
            if result not in cache: #cut down on duplicates
                cache.append(result)
        return self.data
    
x = GetData()
house_info = x.get('house')
congress_info = x.get('congress')
senate_info = x.get('senate')
#print(type(senate_info))
#print(type(cache))
for dict in cache:
    for ticker in dict: