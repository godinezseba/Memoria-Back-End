from ariadne import load_schema_from_path, make_executable_schema

from .queries import queries
from .mutations import mutations
from .resolvers import resolvers
from .resolvers.Product import *
from .resolvers.Company import *

loaded_schema = load_schema_from_path('./Products/')
