def connection_tuple_to_dict(tuple):
    array = []
    for i in range(len(tuple)):
        connection = {
        "uuid": tuple[i][0],
        "basepoint_1_uuid": tuple[i][1],
        "basepoint_2_uuid": tuple[i][2],
        "weight": tuple[i][3],
        "floor_number": tuple[i][4],
        }
        array.append(connection)
    return array