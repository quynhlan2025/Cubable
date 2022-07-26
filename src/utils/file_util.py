import os
import shutil
import time

from src.utils import logger


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def create_file(file_path):
    open(file_path, 'w')


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def read_file(file_path) -> str:
    with open(file_path, 'r', encoding='utf8') as my_file:
        return my_file.read()


def is_file_exist(file_path):
    return os.path.exists(file_path)


def is_file_exist_in_time(file_path, time_to_wait=10):
    time_counter = 0
    flag = True
    while (os.path.exists(file_path) == False):
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            flag = False
            break
    return flag


def read_properties_file(file_path):
    separator = "="
    keys = {}
    try:
        with open(file_path, 'r', encoding='utf8') as data:
            for line in data:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    keys[name.strip()] = value.strip()
        return keys
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return None
