from ariadne import QueryType, ObjectType

query = QueryType()
mutation = ObjectType('Mutation')
user = ObjectType('User')

resolvers = [query, mutation, user]
