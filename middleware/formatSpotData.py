import json
from geojson import Point, Feature, FeatureCollection, dump

def formatLosAngeles(data):
    features = []
    for datum in data:
        point =  Point((datum[7], datum[6], 0.0))
        features.append(Feature(geometry=point, properties={ "spot_id": datum[0], "block_face": datum[1], "meter_type": datum[2], "rate_type": datum[3], "rate_range": datum[4], "meter_time_limit": datum[5], "event_time_utc": datum[9]}))

# add more features...
# features.append(...)

    feature_collection = FeatureCollection(features)
    print(type(feature_collection))
    return feature_collection

def formatSanFrancisco(data):
    #features = []
    ###features.append(Feature(geometry=point, properties={}))
    data = json.loads(json.dumps(data))
    print(type(data))
    return data

# add more features...
# features.append(...)

    feature_collection = FeatureCollection(features)
    return feature_collection