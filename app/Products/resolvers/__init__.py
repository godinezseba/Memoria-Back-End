from ariadne import QueryType, ObjectType

query = QueryType()
mutation = ObjectType('Mutation')
certifier = ObjectType('Certifier')
company = ObjectType('Company')
product = ObjectType('Product')

resolvers = [query, mutation, certifier, company, product]
