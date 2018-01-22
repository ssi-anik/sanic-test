from sanic.response import text

from framework.models import User


class Controller(object):
    def postUserRating(request):
        users = User.Model.where('id', 1).get()
        return text("Not passed" if not users else "Passed")

    def updateUserRating(request, user_id):
        pass

    def getEntityRating(request, entity_id):
        pass
