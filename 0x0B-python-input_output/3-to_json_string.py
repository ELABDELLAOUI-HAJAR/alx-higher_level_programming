#!/usr/bin/python3
"""Define to_json_string function"""
import json


def to_json_string(my_obj):
    """Definition of to_json_string function
    Args:
        my_obj: the object to be serialized
    Return: the JSON representation of the obj
    """
    return json.dumps(my_obj)
