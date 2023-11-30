import json


DOCKER_CONFIG_PATH = '/Users/karlhajjar/.docker/config.json'


def load_json(path):
    with open(path, "r") as json_file:
        data = json.load(json_file)
    return data


def dump_json(dic, path):
    with open(path, "w") as outfile:
        json.dump(dic, outfile)


def check_json_config():
    print('Loading json config from :', DOCKER_CONFIG_PATH)
    json_config = load_json(DOCKER_CONFIG_PATH)
    print('Loaded json config :\n', json_config)
    print('')
    json_config["credStore"] = "desktop"
    if "credsStore" in json_config.keys():
        print('Removing corrupted key credsStore from docker json config')
        json_config.pop("credsStore")

    dump_json(json_config, DOCKER_CONFIG_PATH)
    print('Dumped json config:\n', json_config)
    print('')

