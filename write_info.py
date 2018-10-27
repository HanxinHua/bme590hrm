import json


def write_info(file_name, file_info):
    """
    :Synopsis: Generate a file with information
    :param file_name: The name of the output file
    :param file_info: Information to store in the file
    """
    with open('{}.json'.format(file_name), 'w') as fp:
        json.dump(file_info, fp, indent=4, sort_keys=True)
