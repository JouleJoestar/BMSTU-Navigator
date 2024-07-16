def room_tuple_to_dict(tuple):
    array = []
    for i in range(len(tuple)):
        room = {
        "uuid": tuple[i][0],
        "displayed_name": tuple[i][1],
        "private_name": tuple[i][2],
        "description": tuple[i][3],
        "room_type": tuple[i][4],
        "coordinates": tuple[i][5],
        "floor_id": tuple[i][6],
        "basepoint_uuid" : tuple[i][7]
        }
        array.append(room)
    return array