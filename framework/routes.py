from sanic.exceptions import NotFound
from controller import Controller
from sanic.response import json


def include_routes(app):
    app.add_route(uri='/users/<user_id:int>', handler=Controller.postUserRating, methods=['POST'],
                  name='postUserRating')
    app.add_route(uri='/users/<user_id:int>', handler=Controller.updateUserRating, methods=['PATCH'],
                  name='updateUserRating')
    app.add_route(uri='/entity/<entity_id:int>', handler=Controller.getEntityRating, methods=['GET'],
                  name='postUserRating')

    @app.exception(NotFound)
    async def notFoundException(request, exception):
        return json({"status": "Not found", "error": True}, status=404)
