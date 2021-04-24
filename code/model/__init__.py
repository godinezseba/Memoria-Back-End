from flask_restx import Api

api = Api(version='1.0',
    title='Cloud Impact Rating API',
    description='A protoype API system allowing the storage and retrieval of Climate Impact Rating data for products',
    prefix='/v1'
)
