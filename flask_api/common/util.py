import psycopg2
import os
from flask_restful import reqparse
import uuid

def get_db_connection():
    # # версия для работы в контейнере
    # connection = psycopg2.connect(host = os.getenv("HOST_NAME"),
    #                               database = os.getenv("DATABASE_NAME"),
    #                               user = os.getenv("USER_NAME"),
    #                               port = os.getenv("BACKEND_PORT_POSTGRES"),
    #                               password = os.getenv("PASSWORD_POSTGRES"))


    # версия для работы вне контейнера (в случае, если проблемы с кодировкой при импорте переменных окружения)
    connection = psycopg2.connect(host = 'localhost',
                            database = 'BMSTU_Navigator_TEST',
                            user = 'postgres',
                            port = 5432,
                            password = 'postgres')


    return  connection

def get_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('uuid')
    parser.add_argument('floor_uuid')
    parser.add_argument('coordinates')
    parser.add_argument('node_uuid')
    parser.add_argument('weight')
    parser.add_argument('displayed_name')
    parser.add_argument('private_name')
    parser.add_argument('description')
    parser.add_argument('floor_count')
    return parser

def find_polygon_center(vertices):
    num_vertices = len(vertices)
    
    # Инициализация суммарных значений координат
    sum_x = 0
    sum_y = 0
    
    # Суммирование значений координат
    for vertex in vertices.values():
        sum_x += int(vertex['x'])
        sum_y += int(vertex['y'])
    
    # Нахождение средних значений координат
    center_x = sum_x / num_vertices
    center_y = sum_y / num_vertices
    
    return center_x, center_y

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_int_convertible(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def is_uuid(s):
    try:
        uuid_obj = uuid.UUID(s)
        return True
    except ValueError:
        return False