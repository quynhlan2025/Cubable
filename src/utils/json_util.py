import json
from typing import Any


def load(json_file_location: str) -> Any:
    with open(json_file_location, encoding='utf8') as json_file:
        json_data = json.load(json_file)
    return json_data


def dump(json_file_location, json_object):
    with open(json_file_location, "w") as json_file:
        json.dump(json_object, json_file)


def format_string(string: str) -> dict:
    # Format a string to a json dict data type
    return json.loads(string)


def format_json_to_str(json_data: str) -> str:
    # Format a string to a json format string
    return json.dumps(json_data, indent=4, ensure_ascii=False)


def format(data: dict) -> str:
    # Convert a dict type to json type
    return json.dumps(data, ensure_ascii=False)
