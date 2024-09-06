from flask_api.resources.db_scripts.db_query import postgresql_select_AllRoomsInTheBuildingAdmin, \
    postgresql_select_AllBasePointsInTheBuildingAdmin, postgresql_select_FloorByBuildingUuidAndFloorNumber, \
    postgresql_select_AllBasePointsConnectionsAdmin, postgresql_select_Floors_by_Building_UuidAdmin, \
    postgresql_select_GetFloorCount, postgresql_select_RoomsInTheBuildingByFloorAdmin, \
    postgresql_select_BasePointsInTheBuildingByFloorAdmin, postgresql_select_BasePointsConnectionsByFloorAdmin
from flask_api.models.Floors_model import floor_tuple_to_dict, floor_tuple_to_dict__Admin
from flask_api.models.Connections_model import connection_tuple_to_dict
from flask_api.models.Rooms_model import room_tuple_to_dict__Admin
from flask_api.common.util import is_int_convertible, is_uuid
from flask_api.models.BaseNodes_model import basenode_tuple_to_dict__Admin
from flask_restful import Resource
from flask import Flask, request


class GetAdminDataByBuildingUuid(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self, building_uuid):
        print(building_uuid)
        str_building_uuid = str(building_uuid)

        self.cursor.execute(postgresql_select_Floors_by_Building_UuidAdmin, (str_building_uuid,))
        floor_record = self.cursor.fetchall()

        self.cursor.execute(postgresql_select_AllRoomsInTheBuildingAdmin, (str_building_uuid,))
        room_record = self.cursor.fetchall()

        self.cursor.execute(postgresql_select_AllBasePointsInTheBuildingAdmin, (str_building_uuid,))
        basenode_record = self.cursor.fetchall()

        self.cursor.execute(postgresql_select_AllBasePointsConnectionsAdmin, (str_building_uuid,))
        connection_record = self.cursor.fetchall()

        floor_dict = {}
        room_dict = {}
        basenode_dict = {}
        connection_dict = {}

        if floor_record != []:
            floor_dict = floor_tuple_to_dict(floor_record)

        if room_record != []:
            room_dict = room_tuple_to_dict__Admin(room_record)

        if basenode_record != []:
            basenode_dict = basenode_tuple_to_dict__Admin(basenode_record)

        if connection_record != []:
            connection_dict = connection_tuple_to_dict(connection_record)

        result = {
        "floors": floor_dict,
        "rooms": room_dict,
        "basenodes": basenode_dict,
        "connections": connection_dict
        }

        return result

class GetAdminDataByBuildingUuidSplitedByFloors(Resource):
    def __init__(self, **kwargs):
        self.cursor = kwargs['cursor']

    def get(self, building_uuid):
        print(building_uuid)
        str_building_uuid = str(building_uuid)

        self.cursor.execute(postgresql_select_GetFloorCount, (str_building_uuid,))
        floor_count_record = self.cursor.fetchall()
        floor_count = floor_count_record[0][0]

        floor_array =[]

        for i in range(floor_count - 2):
            current_floor_number = i + 1

            self.cursor.execute(postgresql_select_FloorByBuildingUuidAndFloorNumber, (str_building_uuid, current_floor_number,))
            floor_record = self.cursor.fetchall()

            self.cursor.execute(postgresql_select_RoomsInTheBuildingByFloorAdmin, (str_building_uuid, current_floor_number,))
            room_record = self.cursor.fetchall()

            self.cursor.execute(postgresql_select_BasePointsInTheBuildingByFloorAdmin, (str_building_uuid, current_floor_number,))
            basenode_record = self.cursor.fetchall()

            self.cursor.execute(postgresql_select_BasePointsConnectionsByFloorAdmin, (str_building_uuid, current_floor_number,))
            connection_record = self.cursor.fetchall()

            floor_dict = {}
            room_dict = {}
            basenode_dict = {}
            connection_dict = {}

            if floor_record != []:
                floor_dict = floor_tuple_to_dict__Admin(floor_record)

            if room_record != []:
                room_dict = room_tuple_to_dict__Admin(room_record)

            if basenode_record != []:
                basenode_dict = basenode_tuple_to_dict__Admin(basenode_record)

            if connection_record != []:
                connection_dict = connection_tuple_to_dict(connection_record)

            data_to_append = {
            "floor": floor_dict,
            "rooms": room_dict,
            "basenodes": basenode_dict,
            "connections": connection_dict
            }

            floor_array.append(data_to_append)

        for i in {111, 222}:
            self.cursor.execute(postgresql_select_FloorByBuildingUuidAndFloorNumber, (str_building_uuid, i,))
            floor_record = self.cursor.fetchall()

            self.cursor.execute(postgresql_select_BasePointsConnectionsByFloorAdmin, (str_building_uuid, i,))
            connection_record = self.cursor.fetchall()

            floor_dict = {}
            connection_dict = {}

            if floor_record != []:
                floor_dict = floor_tuple_to_dict__Admin(floor_record)

            if connection_record != []:
                connection_dict = connection_tuple_to_dict(connection_record)

            data_to_append = {
            "floor": floor_dict,
            "connections": connection_dict
            }

            floor_array.append(data_to_append)


        return floor_array





