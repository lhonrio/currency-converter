from flask_restx import fields
from src.server.instance import server

#Input of Price
real = server.api.model('Value', {
    'value': fields.Float(description='Value in Reais')
})

#Output of Price
currency_value = server.api.model('Value', {
    'USD': fields.Float(description="Value in USD"),
    'EUR': fields.Float(description="Value in EUR"),
    'GBP': fields.Float(description="Value in GBP")
})



