import json


def dump_json(path, j):
    with open(path, 'w') as f:
        json.dump(j, f)


def load_json(path):
    with open(path) as f:
        j = json.load(f)
    return j
