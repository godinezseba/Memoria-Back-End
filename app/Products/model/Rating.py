from flask_restx import fields

from app.api import api

RatingModel = api.model('Rating', {
    'efficiency': fields.Integer(description='The efficiency-in-use rating (0-9, where 0 is best) of this item'),
    'energy': fields.Float(description='The energy (J) to produce this item'),
    'CO2': fields.Float(description='The CO2 released (Kg) to produce this item'),
    'water': fields.Float(description='The volume of water (litres) to produce this item'),
    # 'otherGG': fields.Float(description='The other green house gases released (Kg) to produce this item'),
    # 'plastic': fields.Float(description='The amout of plastic (Kg) included in this item'),
    # 'recyclability': fields.Integer(description='The recyclability rating (0-9, where 0 is best) of this item'),
    # 'repairability': fields.Integer(description='The Right to Repair rating (0-9, where 0 is best) of this item')
})

# GraphQL schema
rating = """
  type Rating {
    efficiency: Int
    energy: Int
    CO2: Int
    water: Int
  }
"""
