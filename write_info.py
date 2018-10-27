import json


def write_info(file_name, file_info):
    """
    :param file_name: The name of the output file
    :param file_info: Information to store in the file
    :Synopsis: Generate a file with information
    """
    with open('{}.json'.format(file_name), 'w') as fp:
        json.dump(file_info, fp, indent=4, sort_keys=True)
