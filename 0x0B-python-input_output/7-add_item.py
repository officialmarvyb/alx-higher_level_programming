#!/usr/bin/python3
"""
Load, add, save module
"""
import sys
import json

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    new = load_json(file)
except (ValueError, FileNotFoundError):
    new = []

for args in sys.argv[1:]:
    new.append(args)

# Save the list as a JSON representation in the add_item.json file
save_json(new, file)
