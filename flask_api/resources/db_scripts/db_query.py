
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
postgresql_select_FloorByBuildingUuidAndFloorNumber = """SELECT * FROM public.floor WHERE building_uuid = %s and floor_number = %s"""
postgresql_select_AllBasePointsConnections = """SELECT basepoint_1_uuid, basepoint_2_uuid, weight FROM public.base_connection """
postgresql_select_BasePoint_by_Uuid = """SELECT * FROM public.basepoint WHERE  basepoint_uuid = %s """
postgresql_select_only_coords_from_BasePoint_by_Uuid = """SELECT coordinates FROM public.basepoint WHERE  basepoint_uuid = %s """
#postgresql_select_Floors_by_Building_Uuid = """SELECT * FROM public.floor WHERE  building_uuid = %s ORDER BY floor_number"""
postgresql_select_Floors_by_Building_Uuid = """SELECT * FROM public.floor WHERE  building_uuid = %s and display_flag = true ORDER BY floor_number"""
postgresql_select_BasePoint_Connections_by_BasePointUuid = """SELECT * FROM public.base_connection WHERE  basepoint_1_uuid = %s """
postgresql_select_Floors_by_Building_UuidAdmin = """SELECT * FROM public.floor 
                                                    WHERE  building_uuid = %s 
                                                    ORDER BY floor_number"""
postgresql_select_AllRoomsInTheBuildingAdmin = """SELECT r.room_uuid, r.displayed_name, r.private_name, r.floor_uuid, f.floor_number, r.basepoint_uuid, r.coordinates, r.description, r.room_type
                                                FROM public.room AS r
                                                JOIN public.floor AS f ON r.floor_uuid = f.floor_uuid
                                                WHERE f.building_uuid = %s
                                                ORDER BY f.floor_number, r.displayed_name;
                                                """
postgresql_select_AllBasePointsInTheBuildingAdmin = """ SELECT bp.basepoint_uuid, bp.displayed_name, bp.private_name, f.floor_number, bp.floor_uuid, bp.basenode_type, bp.coordinates
                                                FROM public.basepoint AS bp
                                                JOIN public.floor AS f ON bp.floor_uuid = f.floor_uuid
                                                WHERE f.building_uuid = %s
                                                ORDER BY f.floor_number, bp.displayed_name; 
                                                """
postgresql_select_AllBasePointsConnectionsAdmin = """SELECT bc.base_connection_uuid, bc.basepoint_1_uuid, bc.basepoint_2_uuid, bc.weight, f.floor_number 
                                                     FROM public.base_connection AS bc
                                                     JOIN public.floor AS f ON bc.floor_uuid = f.floor_uuid
                                                     WHERE f.building_uuid = %s
                                                     ORDER BY f.floor_number;
                                                     """

postgresql_select_GetFloorCount = """ SELECT count(*) 
                                      FROM public.floor AS f 
                                      WHERE f.building_uuid = %s
                                      """

postgresql_select_RoomsInTheBuildingByFloorAdmin = """SELECT r.room_uuid, r.displayed_name, r.private_name, r.floor_uuid, f.floor_number, r.basepoint_uuid, r.coordinates, r.description, r.room_type
                                                FROM public.room AS r
                                                JOIN public.floor AS f ON r.floor_uuid = f.floor_uuid
                                                WHERE f.building_uuid = %s and f.floor_number = %s
                                                ORDER BY f.floor_number, r.displayed_name;
                                                """
postgresql_select_BasePointsInTheBuildingByFloorAdmin = """ SELECT bp.basepoint_uuid, bp.displayed_name, bp.private_name, f.floor_number, bp.floor_uuid, bp.basenode_type, bp.coordinates
                                                FROM public.basepoint AS bp
                                                JOIN public.floor AS f ON bp.floor_uuid = f.floor_uuid
                                                WHERE f.building_uuid = %s and f.floor_number = %s
                                                ORDER BY f.floor_number, bp.displayed_name; 
                                                """
postgresql_select_BasePointsConnectionsByFloorAdmin = """SELECT bc.base_connection_uuid, bc.basepoint_1_uuid, bc.basepoint_2_uuid, bc.weight, f.floor_number 
                                                     FROM public.base_connection AS bc
                                                     JOIN public.floor AS f ON bc.floor_uuid = f.floor_uuid
                                                     WHERE f.building_uuid = %s and f.floor_number = %s
                                                     ORDER BY f.floor_number;
                                                     """


#insert queries
postgresql_insert_BasePoint_Connection = """INSERT INTO base_connection(weight, basepoint_1_uuid, basepoint_2_uuid, floor_uuid)
                                                 VALUES (%s, %s, %s, %s);"""
postgresql_insert_BasePoint = """INSERT INTO basepoint(floor_uuid, coordinates)
                                                 VALUES (%s, %s);"""
postgresql_insert_Building = """INSERT INTO building(displayed_name, private_name, description, floor_count)
                                                 VALUES (%s, %s, %s, %s);"""