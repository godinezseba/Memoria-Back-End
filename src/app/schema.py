from ariadne import make_executable_schema
from ariadne import load_schema_from_path

from app.Products.queries import queries as products_queries
from app.Users.queries import queries as users_queries

from app.Products.mutations import mutations as products_mutations
from app.Users.mutations import mutations as users_mutations

from app.Products.resolvers import resolvers as products_resolvers
from app.Users.resolvers import resolvers as users_resolvers

from app.Products.resolvers.Product import *
from app.Products.resolvers.Company import *
from app.Users.resolvers.User import *

products_loaded_schema = load_schema_from_path('./app/Products/')
users_loaded_schema = load_schema_from_path('./app/Users/')

queries = f"""
  scalar JSON
  type Query {{
    {products_queries}
    {users_queries}
  }}
"""

mutations = f"""
  type Mutation {{
    {products_mutations}
    {users_mutations}
  }}
"""

executable_schema = make_executable_schema(
    [
        queries,
        mutations,
        products_loaded_schema,
        users_loaded_schema,
    ],
    [
        *products_resolvers,
        *users_resolvers,
    ])
