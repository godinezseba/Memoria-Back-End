from ariadne import QueryType, ObjectType

query = QueryType()
mutation = ObjectType('Mutation')
product = ObjectType('Product')
company = ObjectType('Company')

resolvers = [query, mutation, product, company]
