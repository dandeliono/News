import time;
def timestamp_from_objectid(objectid):
    result = 0
    try:
        result = time.mktime(objectid.generation_time.timetuple())
    except:
        pass
    return result