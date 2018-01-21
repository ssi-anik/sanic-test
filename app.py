from json import dumps

from gunicorn.http import body
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.response import json, text
from controller import Controller

app = Sanic()


app.add_route(uri='/users/<user_id:int>', handler=Controller.postUserRating, methods=['POST'], name='postUserRating')
app.add_route(uri='/users/<user_id:int>', handler=Controller.updateUserRating, methods=['PATCH'], name='updateUserRating')
app.add_route(uri='/entity/<entity_id:int>', handler=Controller.getEntityRating, methods=['GET'], name='postUserRating')

# @app.route('/users/<user_id:int>', methods=['POST'])
# async def user_id_handler(request, user_id):
#     return text("Users {}.".format(user_id))
#
#
# @app.route('/tag/<tag>')
# async def tag_handler(request, tag):
#     return text('Tag - {}'.format(tag))


@app.exception(NotFound)
async def notFoundException(request, exception):
    return json({"status": "Not found", "error": True}, status=404)

# @app.exception(MethodNotSupported)
# async def notFound(request):
#     return json({"status": "Not found", "error": True}, 404)
