#!/usr/bin/python3
""" this script saves cmd argv to a list then to a json file """


if __name__ == "__main__":
    import sys

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").\
        load_from_json_file
    try:
        items = load_from_json_file("add_item.json")
    except:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
