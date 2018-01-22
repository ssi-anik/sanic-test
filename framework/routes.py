from sanic.exceptions import NotFound, ServerError
from sanic.response import json

from framework.controller import Controller


def include_routes(app):
    app.add_route(uri='/', handler=Controller.postUserRating, methods=['POST'], name='postUserRating')

    @app.exception(NotFound)
    async def notFoundException(request, exception):
        return json({"status": "Not found", "error": True}, status=404)

    @app.exception(ServerError)
    async def serverErrorException(request, exception):
        return json({'status': "Something went wrong!", 'error': True}, status=500)
