from ariadne import make_executable_schema

from Products import loaded_schema as products_loaded_schema
from Users import loaded_schema as users_loaded_schema

from Products import resolvers as products_resolvers
from Users import resolvers as users_resolvers

print([
    products_loaded_schema,
    users_loaded_schema,
], flush=True)

executable_schema = make_executable_schema(
    [
        products_loaded_schema,
        users_loaded_schema,
    ],
    [
        *products_resolvers,
        *users_resolvers,
    ])
