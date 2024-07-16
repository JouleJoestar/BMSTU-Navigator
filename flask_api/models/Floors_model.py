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