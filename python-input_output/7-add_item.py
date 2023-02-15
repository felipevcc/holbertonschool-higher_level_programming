#!/usr/bin/python3
"""Script that adds all args to a list, and then saves them to a file"""
import sys
import json

"""Json functions"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Constants"""
ARGS = sys.argv[1:]
FILENAME = "add_item.json"


def main():
    """Load file contents"""
    try:
        file_content = load_from_json_file(FILENAME)
    except FileNotFoundError:
        file_content = []

    """Update content"""
    file_content += ARGS

    """Save content"""
    save_to_json_file(file_content, FILENAME)


if __name__ == '__main__':
    main()
