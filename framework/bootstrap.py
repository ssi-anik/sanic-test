from sanic import Sanic

from framework.routes import include_routes
from framework.connection import db

# instantiate the sanic application
app = Sanic()
# include the routes
include_routes(app)
