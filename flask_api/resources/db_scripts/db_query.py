
#select queries
postgresql_select_RoomBasePoint = """SELECT basepoint_uuid, floor_uuid FROM public.room WHERE room_uuid = %s """
postgresql_select_AllRoomsInTheBuilding = """SELECT * FROM public.room, public.floor WHERE building_uuid = %s and room.floor_uuid = floor.floor_uuid ORDER BY floor_number, room.displayed_name """
postgresql_select_AllCoords = """SELECT room_uuid, coordinates FROM room """
postgresql_select_RoomCoordinates = """SELECT coordinates FROM public.room WHERE room_uuid = %s """
postgresql_select_AllBasePoints = """SELECT * FROM public.basepoint"""
postgresql_select_AllBasePointsAtTheFloor = """SELECT * FROM public.basepoint WHERE floor_uuid = %s """
postgresql_select_AllRoomsAtTheFloor = """SELECT * FROM public.room WHERE floor_uuid = %s """
postgresql_select_AllBasePointsAtTheFloorNoFloorUuid = """SELECT * FROM public.basepoint"""
postgresql_select_AllBuildings = """SELECT * FROM public.building """
postgresql_select_FloorUuidByBuildingUuidAndFloorNumber = """SELECT floor_uuid FROM public.floor WHERE building_uuid = %s and floor_number = %s"""
postgresql_select_AllBasePointsConnections = """SELECT basepoint_1_uuid, basepoint_2_uuid, weight FROM public.base_connection """
postgresql_select_BasePoint_by_Uuid = """SELECT * FROM public.basepoint WHERE  basepoint_uuid = %s """
postgresql_select_only_coords_from_BasePoint_by_Uuid = """SELECT coordinates FROM public.basepoint WHERE  basepoint_uuid = %s """
#postgresql_select_Floors_by_Building_Uuid = """SELECT * FROM public.floor WHERE  building_uuid = %s ORDER BY floor_number"""
postgresql_select_Floors_by_Building_Uuid = """SELECT * FROM public.floor WHERE  building_uuid = %s and display_flag = true ORDER BY floor_number"""
postgresql_select_BasePoint_Connections_by_BasePointUuid = """SELECT * FROM public.base_connection WHERE  basepoint_1_uuid = %s """

#insert queries
postgresql_insert_BasePoint_Connection = """INSERT INTO base_connection(weight, basepoint_1_uuid, basepoint_2_uuid, floor_uuid)
                                                 VALUES (%s, %s, %s, %s);"""
postgresql_insert_BasePoint = """INSERT INTO basepoint(floor_uuid, coordinates)
                                                 VALUES (%s, %s);"""
postgresql_insert_Building = """INSERT INTO building(displayed_name, private_name, description, floor_count)
                                                 VALUES (%s, %s, %s, %s);"""