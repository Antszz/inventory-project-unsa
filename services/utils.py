from fake_db import FAKE_DB


def get_objects(type):
    return [object for object in FAKE_DB if object['type'] == type and not object.get('delete')]
