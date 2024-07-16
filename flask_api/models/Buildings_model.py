def building_tuple_to_dict(tuple):
    array = []
    for i in range(len(tuple)):
        building = {
            "uuid": tuple[i][0],
            "displayed_name": tuple[i][1],
            "private_name": tuple[i][2],
            "describtion": tuple[i][3],
            "floor_count": tuple[i][3]
        }
        array.append(building)
    return array