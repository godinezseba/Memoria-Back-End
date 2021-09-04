from ariadne import QueryType, ObjectType

query = QueryType()
mutation = ObjectType('Mutation')
action = ObjectType('Action')
certificate = ObjectType('Certificate')
certifier = ObjectType('Certifier')
company = ObjectType('Company')
product = ObjectType('Product')

resolvers = [query, mutation, certifier, company, product, action, certificate]
