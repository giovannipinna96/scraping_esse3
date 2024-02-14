import json


def read_json(filename):
    """
    Read JSON data from a file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data.
    """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data
