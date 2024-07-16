from flask_api.resources.db_scripts.db_query import postgresql_select_AllCoords
from flask_restful import Resource

class GetAllCoords(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):

        self.cursor.execute(postgresql_select_AllCoords)
        coords = self.cursor.fetchall()
        return coords