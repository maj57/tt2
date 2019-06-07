#!/usr/bin/env python3

import json, requests
from mappers import Database


class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        # SELECT password FROM users WHERE username='{submitted_username}';
        with Database() as d:
            d.cursor.execute(
                f'''SELECT password
                    FROM users
                    WHERE username='{self.username}';''')
            password = d.cursor.fetchone()[0]
            if password:
                if self.password == password:
                    return True
            return False
def lookup(company):
    company = company
    api = lookup_api()
    query = api + company
    return json.loads(requests.get(query).text)[0]['Symbol']

def quote(symbol):
    symbol = symbol
    api = quote_api()
    query = api + symbol
    return json.loads(requests.get(query).text)['LastPrice']
    
        
def quote_api():
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=' 
    return endpoint
def lookup_api():
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='
    return endpoint
    
if __name__ == '__main__':
    #user = User('cookiemonster','opensesame')
    #print(user.login())
    symbol = input('stock :')
    company = input('company:')
    lookup(company)
    print(quote(symbol))
