from sanic.response import text


class Controller(object):
    def postUserRating(request, user_id):
        return text("Passed")

    def updateUserRating(request, user_id):
        pass

    def getEntityRating(request, entity_id):
        pass