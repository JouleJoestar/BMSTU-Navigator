from flask_api.resources.db_scripts.db_query import postgresql_select_RoomBasePoint, postgresql_select_AllBasePoints,\
    postgresql_select_AllBasePointsConnections, postgresql_select_RoomCoordinates, postgresql_select_AllRoomsInTheBuilding
from flask_restful import Resource, reqparse
from flask_api.models.Rooms_model import room_tuple_to_dict
from flask_api.common.util import is_int_convertible, is_uuid
import networkx as nx
from flask import Flask, request

class GetPath(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):
        G = nx.DiGraph()

        initial_point = str(request.args.get('from'))
        finish_point = str(request.args.get('to'))

        if (not is_uuid(initial_point) or  not is_uuid(finish_point)):
            return "Bad request", 400

        self.cursor.execute(postgresql_select_RoomBasePoint, (initial_point,))
        initial_basepoint_record = self.cursor.fetchall()

        print("initial_basepoint_record", initial_basepoint_record)

        if initial_basepoint_record != []:
            initial_basepoint = initial_basepoint_record[0][0]
            initial_basepoint_floor_uuid = initial_basepoint_record[0][1]
        else:
            return "Initial point record not found", 404

        self.cursor.execute(postgresql_select_RoomBasePoint, (finish_point,))
        finish_basepoint_record = self.cursor.fetchall()

        if finish_basepoint_record != []:
            finish_basepoint = finish_basepoint_record[0][0]
            finish_basepoint_floor_uuid = finish_basepoint_record[0][1]
        else:
            return "Finish point record not found", 404

        self.cursor.execute(postgresql_select_AllBasePoints)
        all_basepoints_record = self.cursor.fetchall()

        if all_basepoints_record != []:
            for i in range(len(all_basepoints_record)):
                G.add_node(all_basepoints_record[i][0], floor_uuid=all_basepoints_record[i][4])

            self.cursor.execute(postgresql_select_AllBasePointsConnections)
            all_basepointconnections_record = self.cursor.fetchall()

            if all_basepointconnections_record != []:
                for i in range(len(all_basepointconnections_record)):
                    G.add_edge(all_basepointconnections_record[i][0], all_basepointconnections_record[i][1], weight=all_basepointconnections_record[i][2])
                path = nx.shortest_path(G, initial_basepoint, finish_basepoint, weight='weight')
                print("shortest parth = " + str(path))
                length = nx.shortest_path_length(G, initial_basepoint, finish_basepoint, weight='weight')
                print("lenth of the shortest parth = " + str(length))
            else:
                return "BasePointsConnections records not found", 404
        else:
            return "BasePoints records not found", 404
        path_with_floor_uuid = [{'floor_uuid': G.nodes[vertex]['floor_uuid'], 'basenode_uuid': vertex} for vertex in path]
        initial_with_floor_uuid = {'floor_uuid': initial_basepoint_floor_uuid, 'room_uuid': initial_point}
        finish_point_with_floor_uuid = {'floor_uuid': finish_basepoint_floor_uuid, 'room_uuid': finish_point}
        return ({'from': initial_with_floor_uuid, 'to': finish_point_with_floor_uuid, 'path' : path_with_floor_uuid, 'lenth': length })

class GetRoomBasePoint(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):

            uuid = request.args.get('uuid')
            self.cursor.execute(postgresql_select_RoomBasePoint, (uuid,))
            basepoint_record = self.cursor.fetchall()
            if basepoint_record != []:
                basepoint = basepoint_record[0][0]
                return basepoint
            else:
                return "Record not found", 404

class GetAllRoomsInTheBuilding(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):
            uuid = request.args.get('uuid')
            self.cursor.execute(postgresql_select_AllRoomsInTheBuilding, (uuid,))
            room_record = self.cursor.fetchall()
            if room_record != []:
                rooms_dict = room_tuple_to_dict(room_record)
                return {"rooms": rooms_dict }
            else:
                return "Record not found", 404




class GetRoomCoordinates(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self):
            uuid = request.args.get('uuid')

            self.cursor.execute(postgresql_select_RoomCoordinates, (uuid,))
            coords_record = self.cursor.fetchall()
            if coords_record != []:
                coords = coords_record[0][0]
                return coords
            else:
                return "Record not found", 404
            
