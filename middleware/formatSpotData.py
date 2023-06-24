import json
from geojson import Point, Feature, FeatureCollection, dump

# Formatting data for /losangeles route
def formatLosAngeles(data):
    features = []
    for datum in data:
        point =  Point((float(datum['Long']), float(datum['Lat']), 0.0))
        features.append(Feature(geometry=point, properties={ "spot_id": datum['SpaceID'], "block_face": datum['BlockFace'], "meter_type": datum['MeterType'], "rate_type": datum['RateType'], "rate_range": datum['RateRange'], "meter_time_limit": datum['MeteredTimeLimit'], "event_time_utc": '0'}))

# add more features...
# features.append(...)

    feature_collection = FeatureCollection(features)
    return feature_collection


# Formatting data for /losangelesloc route
def formatLosAngelesLoc(data):
    features = []
    for datum in data:
        point =  Point((float(datum['Long']), float(datum['Lat']), 0.0))
        features.append(Feature(geometry=point, properties={ "spot_id": datum['SpaceID'], "block_face": datum['BlockFace'], "meter_type": datum['MeterType'], "rate_type": datum['RateType'], "rate_range": datum['RateRange'], "meter_time_limit": datum['MeteredTimeLimit'], "event_time_utc": '0'}))

# add more features...
# features.append(...)

    feature_collection = FeatureCollection(features)
    return feature_collection

def formatSanFrancisco(data):
    #features = []
    ###features.append(Feature(geometry=point, properties={}))
    data = json.loads(json.dumps(data))
    return data

# add more features...
# features.append(...)

    feature_collection = FeatureCollection(features)
    return feature_collection