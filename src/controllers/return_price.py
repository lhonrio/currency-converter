from flask import Flask
from flask_restx import Api, Resource
from flask_restx.fields import Float
from requests.api import get
from src.models.return_prices import *
from src.server.instance import server
import requests, json

app = server.app
api = server.api

@api.route('/converter')
class Converter(Resource):
    @api.expect(real, validate=True)
    @api.marshal_with(currency_value)
    def get(self, ):

        #API request
        coins = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL")
        coins = coins.json()
        
        #Filtering data
        coin_list = {'USD': coins['USDBRL']['bid'], 'EUR': coins['EURBRL']['bid'], 'GBP': coins['GBPBRL']['bid']}
        
        #Capturing the input JSON
        payload = api.payload
        real = payload['value']

        #Currency Conversion and Character Limit
        value_usd = real / float(coin_list['USD'])
        value_eur = real / float(coin_list['EUR'])
        value_gbp = real / float(coin_list['GBP'])

        #Currency Price 
        currency_value = {'USD': f'{value_usd:.2f}', 'EUR': f'{value_eur:.2f}', 'GBP': f'{value_gbp:.2f}'}
            
        return currency_value