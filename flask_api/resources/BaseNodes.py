import json
from flask_api.resources.db_scripts.db_query import postgresql_insert_BasePoint, postgresql_select_AllBasePointsAtTheFloor, postgresql_select_AllBasePointsAtTheFloorNoFloorUuid,\
    postgresql_select_BasePoint_by_Uuid, postgresql_select_BasePoint_Connections_by_BasePointUuid, postgresql_insert_BasePoint_Connection, postgresql_select_AllBasePointsConnections,\
    postgresql_select_only_coords_from_BasePoint_by_Uuid
from flask_api.models.BaseNodes_model import basenode_tuple_to_dict, basenode_with_connections_tuple_to_dict
from flask_api.common.util import find_polygon_center, manhattan_distance
from flask_restful import Resource, reqparse
from flask import Flask, request

class AddBasePoint(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']
        self.parser = kwargs['parser']

    def post(self):
        args = self.parser.parse_args()
        uuid = args['uuid']
        floor_uuid = args['floor_uuid']
        coordinates = args['coordinates']
       
        coordinates_str = str(coordinates).replace("'", '"')
        json_coordinates = json.dumps(json.loads(coordinates_str))

        self.cursor.execute(postgresql_insert_BasePoint, (floor_uuid, json_coordinates,))

        return "Record was successfully added", 200

class GetAllBasePointsAtTheFloor(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):
        floor_uuid = str(request.args.get('uuid'))
        if (floor_uuid != 'None'):
            self.cursor.execute(postgresql_select_AllBasePointsAtTheFloor,(floor_uuid,))
            basepoints_record = self.cursor.fetchall()
        else:
            self.cursor.execute(postgresql_select_AllBasePointsAtTheFloorNoFloorUuid)
            basepoints_record = self.cursor.fetchall()

        if basepoints_record != []:
           return basenode_tuple_to_dict(basepoints_record)
        else:
            return [] #"Record not found", 404

class GetBaseNodeByUuid(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self, basenode_uuid):
        str_basenode_uuid = str(basenode_uuid)
        self.cursor.execute(postgresql_select_BasePoint_by_Uuid, (str_basenode_uuid,))
        basepoint_record = self.cursor.fetchall()

        self.cursor.execute(postgresql_select_BasePoint_Connections_by_BasePointUuid, (str_basenode_uuid,))
        base_connections_record = self.cursor.fetchall()

        if ((basepoint_record != []) and (base_connections_record != [])):
            return basenode_with_connections_tuple_to_dict(basepoint_record, base_connections_record)
        else:
            return [] #"Record not found", 404

class AddBaseNodeConnection(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']
        self.parser = kwargs['parser']

    def post(self, basenode_uuid):
        args = self.parser.parse_args()

        basenode_uuid = str(basenode_uuid)

        node_to_connect_uuid = args['node_uuid']
        floor_uuid = args['floor_uuid']
        #str_node_to_connect_uuid = str(node_to_connect_uuid)
        #weight = args['weight']
        
        self.cursor.execute(postgresql_select_BasePoint_by_Uuid, (basenode_uuid,))
        
        basepoint_record = self.cursor.fetchall()
        if basepoint_record != []:
            basenode_center_x, basenode_uuid_center_y = find_polygon_center(basepoint_record[0][3])
            self.cursor.execute(postgresql_select_only_coords_from_BasePoint_by_Uuid, (node_to_connect_uuid,))
            node_to_connect_coordinates_record = self.cursor.fetchall()
            print(node_to_connect_coordinates_record[0][0])
            node_to_connect_center_x, node_to_connect_center_y = find_polygon_center(node_to_connect_coordinates_record[0][0])
            weight = manhattan_distance(basenode_center_x, basenode_uuid_center_y, node_to_connect_center_x, node_to_connect_center_y)
            self.cursor.execute(postgresql_insert_BasePoint_Connection, (weight, basenode_uuid, node_to_connect_uuid, floor_uuid,))
            self.cursor.execute(postgresql_insert_BasePoint_Connection, (weight, node_to_connect_uuid, basenode_uuid, floor_uuid,))
        else:
            return [] #"Record not found", 404

        return "Record was successfully added", 200

class GetAllBasePointsConnections(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):

        self.cursor.execute(postgresql_select_AllBasePointsConnections)
        baseconnection_record = self.cursor.fetchall()
        print (baseconnection_record)
        if baseconnection_record != []:
            return baseconnection_record
        else:
            return [] #"Record not found", 404
