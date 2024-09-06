def floor_tuple_to_dict(tuple):
    array = []
    for i in range(len(tuple)):
        floor = {
            "uuid": tuple[i][0],
            "displayed_name": tuple[i][1],
            "private_name": tuple[i][2],
            "describtion": tuple[i][3],
            "building_uuid": tuple[i][4],
            "floor_number": tuple[i][5],
            "display_flag": tuple[i][6]
        }
        array.append(floor)
    return array

def floor_tuple_to_dict__Admin(tuple):

    floor = {
        "uuid": tuple[0][0],
        "displayed_name": tuple[0][1],
        "private_name": tuple[0][2],
        "describtion": tuple[0][3],
        "building_uuid": tuple[0][4],
        "floor_number": tuple[0][5],
        "display_flag": tuple[0][6]
    }

    return floor