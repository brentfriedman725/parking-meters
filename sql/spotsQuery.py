getSpotsLosAngeles = "SELECT * FROM losangeles JOIN losangelesoccupancy ON losangeles.space_id =losangelesoccupancy.space_id WHERE occupancy_state='VACANT'"
getSpotsSanFrancisco = "SELECT * FROM sanfrancisco WHERE ACTIVE_METER_FLAG='U' OR ACTIVE_METER_GLAD='T'"

inputOccupancyLosAngeles = "INSERT INTO losangelesoccupancy (space_id, event_time_utc, occupancy_state) VALUES %s"
inputOccupancySanFrancisco = "INSERT INTO sanfrancisco (OBJECTID, PARKING_SPACE_ID, POST_ID, MS_PAY_STATION_ID, MS_SPACE_NUM, ON_OFFSTREET_TYPE, OSP_ID, JURISDICTION, PM_DISTRICT_ID, BLOCKFACE_ID, ACTIVE_METER_FLAG, METER_TYPE, METER_VENDOR, METER_MODEL, CAP_COLOR, OLD_RATE_AREA, STREET_ID, STREET_NAME, STREET_NUM, LONGITUDE, LATITUDE) VALUES %s"
