DROP TABLE IF EXISTS public.base_connection;
DROP TABLE IF EXISTS public.basepoint;
DROP TABLE IF EXISTS public.building;
DROP TABLE IF EXISTS public.floor;
DROP TABLE IF EXISTS public.path;
DROP TABLE IF EXISTS public.room;

CREATE TABLE IF NOT EXISTS public.base_connection
(
    base_connection_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    weight integer,
    connection_type connection_type,
    basepoint_1_uuid uuid NOT NULL,
    basepoint_2_uuid uuid NOT NULL,
    floor_uuid uuid NOT NULL,
    CONSTRAINT base_connection_pkey PRIMARY KEY (base_connection_uuid),
    CONSTRAINT "BasePoint1" FOREIGN KEY (basepoint_1_uuid)
        REFERENCES public.basepoint (basepoint_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "BasePoint2" FOREIGN KEY (basepoint_2_uuid)
        REFERENCES public.basepoint (basepoint_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "Floor_UUID" FOREIGN KEY (floor_uuid)
        REFERENCES public.floor (floor_uuid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.base_connection
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.basepoint
(
    basepoint_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    displayed_name text COLLATE pg_catalog."default",
    private_name text COLLATE pg_catalog."default",
    coordinates jsonb,
    floor_uuid uuid NOT NULL,
    basenode_type basenode_type,
    CONSTRAINT basepoint_pkey PRIMARY KEY (basepoint_uuid),
    CONSTRAINT "Floor" FOREIGN KEY (floor_uuid)
        REFERENCES public.floor (floor_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.basepoint
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.building
(
    building_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    displayed_name text COLLATE pg_catalog."default",
    private_name text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    floor_count integer,
    CONSTRAINT building_pkey PRIMARY KEY (building_uuid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.building
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.floor
(
    floor_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    displayed_name text COLLATE pg_catalog."default",
    private_name text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    building_uuid uuid NOT NULL,
    floor_number integer,
    display_flag boolean NOT NULL DEFAULT false,
    CONSTRAINT floor_pkey PRIMARY KEY (floor_uuid),
    CONSTRAINT "Building" FOREIGN KEY (building_uuid)
        REFERENCES public.building (building_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.floor
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.path
(
    path_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    path jsonb,
    room_1_uuid uuid NOT NULL,
    room_2_uuid uuid NOT NULL,
    CONSTRAINT path_pkey PRIMARY KEY (path_uuid),
    CONSTRAINT "Room1" FOREIGN KEY (room_1_uuid)
        REFERENCES public.room (room_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "Room2" FOREIGN KEY (room_2_uuid)
        REFERENCES public.room (room_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.path
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.room
(
    room_uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
    displayed_name text COLLATE pg_catalog."default",
    private_name text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    room_type room_type,
    coordinates jsonb,
    floor_uuid uuid NOT NULL,
    basepoint_uuid uuid NOT NULL,
    CONSTRAINT room_pkey PRIMARY KEY (room_uuid),
    CONSTRAINT "BasePoint" FOREIGN KEY (basepoint_uuid)
        REFERENCES public.basepoint (basepoint_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "Floor" FOREIGN KEY (floor_uuid)
        REFERENCES public.floor (floor_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.room
    OWNER to postgres;