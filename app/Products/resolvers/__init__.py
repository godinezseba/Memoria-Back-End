from ariadne import QueryType, ObjectType

query = QueryType()
product = ObjectType('Product')
company = ObjectType('Company')

resolvers = [query, product, company]
