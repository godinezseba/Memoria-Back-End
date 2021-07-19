from ariadne import make_executable_schema

from Products import loaded_schema as products_loaded_schema
from Users import loaded_schema as users_loaded_schema

from Products import queries as products_queries
from Users import queries as users_queries

from Products import resolvers as products_resolvers
from Users import resolvers as users_resolvers

queries = f"""
  type Query {{
    {products_queries}
    {users_queries}
  }}
"""

executable_schema = make_executable_schema(
    [
        queries,
        products_loaded_schema,
        users_loaded_schema,
    ],
    [
        *products_resolvers,
        *users_resolvers,
    ])
