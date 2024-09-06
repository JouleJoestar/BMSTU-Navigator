
############# непосредственно API
import os
import json

from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
from flask import render_template
from flask_cors import CORS
from dotenv import load_dotenv

##################

from .resources.Admin import GetAdminDataByBuildingUuid, GetAdminDataByBuildingUuidSplitedByFloors
from .resources.BaseNodes import AddBasePoint, GetBaseNodeByUuid, GetAllBasePointsConnections, GetAllBasePointsAtTheFloor, AddBaseNodeConnection
from .resources.Buildings import GetAllBuildings, AddBuilding
from .resources.Floors import GetAllFloorsByBuildingUuid, GetAllRoomsAndBasepointsByFloorUuid, GetAllRoomsAndBasepointsByBuildingUuidAndFloorNumber
from .resources.Rooms import GetPath, GetRoomBasePoint, GetRoomCoordinates, GetAllRoomsInTheBuilding
from .resources.Misc import GetAllCoords
from .common.util import get_db_connection, get_parser

##################

SECRET_KEY = os.urandom(32)
load_dotenv()

################### Запросы





##################



app = Flask(__name__)
api = Api(app)
CORS(app) # This will enable CORS for all routes



parser = get_parser()
connection = get_db_connection()
connection.autocommit = True
cursor = connection.cursor()

kwargs_cursor_and_parser = { 'cursor': cursor, 'parser' : parser}
kwargs_cursor = {'cursor': cursor}


api.add_resource(GetAllCoords, '/get_all_coords', resource_class_kwargs=kwargs_cursor)

# Возвращает все этажи строения с данным uuid
api.add_resource(GetRoomCoordinates, '/get_room_coords', resource_class_kwargs=kwargs_cursor_and_parser)

# Возвращает uuid базовой точки, с которой соединено данное помещение
api.add_resource(GetRoomBasePoint, '/get_room_basepoint', resource_class_kwargs=kwargs_cursor_and_parser)

# Возвращает все существующие связи между базовыми точками
api.add_resource(GetAllBasePointsConnections, '/get_all_baseconnections', resource_class_kwargs=kwargs_cursor)

# Возвращает все помещения в здании
api.add_resource(GetAllRoomsInTheBuilding, '/get_all_rooms_in_the_building', resource_class_kwargs=kwargs_cursor)

# Возвращает путь между помещениями с uuid "from" и "to" в виде последовательности uuid базовых точек, по которым нужно пройти,
# чтобы добраться до пункта назначения (путь состоит именно из uuid базовых точек,
# uuid "from" и "to" в массив из uuid базовых точек не включаются, потому что "from" и "to" не базовые точки); также возвращает длину этого пути
api.add_resource(GetPath, '/get_path', resource_class_kwargs=kwargs_cursor_and_parser)

# Добавляет строение в базу данных
api.add_resource(AddBuilding, '/buildings/add_building', resource_class_kwargs=kwargs_cursor_and_parser)

# Возвращает все строения
api.add_resource(GetAllBuildings, '/buildings/get_all_buildings', resource_class_kwargs=kwargs_cursor)

# Возвращает все этажи строения с данным uuid
api.add_resource(GetAllFloorsByBuildingUuid, '/floors/<uuid:building_uuid>', resource_class_kwargs=kwargs_cursor)

# Возвращает все помещения и базовые точки для этажа с заданным floor_uuid
api.add_resource(GetAllRoomsAndBasepointsByFloorUuid, '/floors/get_all', resource_class_kwargs=kwargs_cursor)

# Возвращает все помещения и базовые точки для здания с заданным building_uuid и номером этажа floor_number
api.add_resource(GetAllRoomsAndBasepointsByBuildingUuidAndFloorNumber, '/floors/get_all_2', resource_class_kwargs=kwargs_cursor)

#Добавляет базовую точку в базу данных
api.add_resource(AddBasePoint, '/base_nodes/add_base_point', resource_class_kwargs=kwargs_cursor_and_parser)

#Возвращает информацию о всех базовых точках на этаже. В случае, если парамерт uuid не определён, возвращает все базовые точки со всех этажей
api.add_resource(GetAllBasePointsAtTheFloor, '/base_nodes/get_base_point', resource_class_kwargs=kwargs_cursor_and_parser)

#Возвращает информацию о базовой точке и её связях по её uuid
api.add_resource(GetBaseNodeByUuid, '/base_nodes/<uuid:basenode_uuid>', resource_class_kwargs=kwargs_cursor )

# Этот запрос создает в таблице base_connection строĸу, в ĸоторой описывается связь базовой точĸи с uuid=1 с точĸой переданной в теле запроса (допустим с базовой точĸой с uuid = 3).
# То есть после успешного совершения таĸого запроса у точĸи с uuid = 1 появится связь с точĸой 3 с весом 5,
# а ĸроме того, еще должна появиться связь 3 точĸи с 1 (в обратную сторону с таĸим же весом)
api.add_resource(AddBaseNodeConnection, '/base_nodes/<uuid:basenode_uuid>/connection', resource_class_kwargs=kwargs_cursor_and_parser)

api.add_resource(GetAdminDataByBuildingUuidSplitedByFloors, '/admin_data/<uuid:building_uuid>', resource_class_kwargs=kwargs_cursor )



if __name__ == '__main__':
    app.run(debug=True)
    cursor.close() # судя по всему закрытие соединения с БД нужно вставить сюда, но я на самом деле хз
    connection.close()
    print("Работа сервера завершена")