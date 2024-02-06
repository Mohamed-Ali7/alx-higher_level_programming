#!/usr/bin/python3

"""
This module contains a script that adds all arguments to a Python list,
and then save them to a file
"""

import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []
try:
    obj = load_from_json_file("add_item.json")
    my_list.extend(obj)
except Exception:
    pass

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
