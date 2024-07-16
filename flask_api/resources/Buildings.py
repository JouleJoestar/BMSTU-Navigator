from flask_api.resources.db_scripts.db_query import postgresql_insert_Building, postgresql_select_AllBuildings
from flask_restful import Resource, reqparse
from flask_api.models.Buildings_model import building_tuple_to_dict

class AddBuilding(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']
        self.parser = kwargs['parser']

    def post(self):
        args = self.parser.parse_args()

        displayed_name = args['displayed_name']
        private_name = args['private_name']
        description = args['description']
        floor_count = args['floor_count']

        self.cursor.execute(postgresql_insert_Building, (displayed_name, private_name, description, floor_count))

        return "Record was successfully added", 200


class GetAllBuildings(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):
        self.cursor.execute(postgresql_select_AllBuildings)
        building_record = self.cursor.fetchall()

        print (building_record)
        if building_record != []:
            return building_tuple_to_dict(building_record)
        else:
            return "Record not found", 404