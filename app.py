from sanic import Sanic

from framework.routes import include_routes
# instantiate the sanic application
app = Sanic()
# include the routes
include_routes(app)