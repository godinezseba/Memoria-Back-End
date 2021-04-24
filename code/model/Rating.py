from flask_restx import fields

from . import api

RatingModel = api.model('Rating', {
  'efficiency': fields.Integer(required=False, description='The efficiency-in-use rating (0-9, where 0 is best) of this item'),
  'energy': fields.Float(required=False, description='The energy (J) to produce this item'),
  'CO2': fields.Float(required=False, description='The CO2 released (Kg) to produce this item'),
  'otherGG': fields.Float(required=False, description='The other green house gases released (Kg) to produce this item'),
  'water': fields.Float(required=False, description='The volume of water (litres) to produce this item'),
  'plastic': fields.Float(required=False, description='The amout of plastic (Kg) included in this item'),
  'lifetime': fields.Float(required=False, description='The expected lifetime (years) of this item'),
  'recyclability': fields.Integer(required=False, description='The recyclability rating (0-9, where 0 is best) of this item'),
  'repairability': fields.Integer(required=False, description='The Right to Repair rating (0-9, where 0 is best) of this item')
})
