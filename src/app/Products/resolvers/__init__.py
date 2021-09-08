from ariadne import QueryType, ObjectType

query = QueryType()
mutation = ObjectType('Mutation')

action = ObjectType('Action')
certificate = ObjectType('Certificate')
certifier = ObjectType('Certifier')
company = ObjectType('Company')
file = ObjectType('File')
product = ObjectType('Product')

resolvers = [query, mutation, certifier,
             company, product, action, certificate, file]
