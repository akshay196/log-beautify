#!/usr/bin/env python3
import re
import sys
import os.path


def parse_file(file_name):
    """
    Take file name as input parameter.
    Parse that file for finding urls
    :return: List of urls
    """
    with open(file_name) as file_obj:
        file_content = file_obj.read()

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', file_content)

    return urls


if __name__ == '__main__':
    if os.path.exists(sys.argv[1]):
        urls = parse_file(sys.argv[1])
        if urls:
            for url in urls:
                print(url)
        else:
            print("No url found in log file")
    else:
        print("File not exists")
