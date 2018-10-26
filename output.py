import json


def write_info(file_name, file_info):
    with open('{}.json'.format(file_name), 'w') as fp:
        json.dump(file_info, fp, indent=4, sort_keys=True)


