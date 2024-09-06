def basenode_tuple_to_dict(tuple):
    array = []
    for i in range(len(tuple)):
        base_point = {
        "uuid": tuple[i][0],
        "displayed_name": tuple[i][1],
        "private_name": tuple[i][2],
        "coordinates": tuple[i][3],
        "floor_uuid": tuple[i][4],
        "basenode_type": tuple[i][5]
        }
        array.append(base_point)
    return array

def basenode_with_connections_tuple_to_dict(basenode_tuple, connections_tuple):
    connections = []
    for i in range(len(connections_tuple)):
        connection = {
            "uuid" : connections_tuple[i][0],
            "weight": connections_tuple[i][1],
            "connection_type": connections_tuple[i][2],
            "basepoint_1_uuid": connections_tuple[i][3],
            "basepoint_2_uuid": connections_tuple[i][4],
    }
    connections.append(connection)
    result = {
        "uuid": basenode_tuple[0][0],
        "displayed_name": basenode_tuple[0][1],
        "private_name": basenode_tuple[0][2],
        "coordinates": basenode_tuple[0][3],
        "floor_uuid": basenode_tuple[0][4],
        "basenode_type": tuple[i][5],
        "connections": connections
        }
    return result

def basenode_tuple_to_dict__Admin(tuple):
    array = []
    for i in range(len(tuple)):
        base_point = {
        "uuid": tuple[i][0],
        "displayed_name": tuple[i][1],
        "private_name": tuple[i][2],
        "floor_number": tuple[i][3],
        "floor_uuid": tuple[i][4],
        "basenode_type": tuple[i][5],
        "coordinates": tuple[i][6],
        }
        array.append(base_point)
    return array