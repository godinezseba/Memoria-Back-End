from ariadne import load_schema_from_path

from .resolvers import resolvers
from .resolvers.User import *

loaded_schema = load_schema_from_path('./Users/')
