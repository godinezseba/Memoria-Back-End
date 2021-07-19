from ariadne import QueryType, ObjectType

query = QueryType()
user = ObjectType('User')

resolvers = [query, user]
