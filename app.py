#!/usr/bin/env python3

import sys
import urllib.request
from os import system

# checking systax
if len(sys.argv) < 2:
    print("Failed. \n Wrong input \n")
    exit()

log_url = sys.argv[1]

target = open("index.html", 'w')

def words_to_string(words):
    message = ""
    for word in words:
        message = message + " " + word
    return message

# starting part
target.write("<html><head><title></title><link href='style.css' rel='stylesheet'></head><body><pre>")

with urllib.request.urlopen(log_url) as log:
    for line in log:
        line = line.decode('utf-8')
        words = line.split(" ")
        message = ""
        html_line = "<p><span class='tm'>" + words[0] + "</span> <span class='nick'>" + words[1].strip("<>") + "</span>" + words_to_string(words[2:len(words)])  + "</p>"        
        target.write(html_line)


# Ending part
target.write("</pre></body></html>")

target.close()

#Log Display
print("Success\n See beautiful log at index.html")
response = input("Do you want to open index.html[y/N]: ")
if response == 'y' or response == 'Y' or response == 'yes':
    system("firefox index.html")
else:
    exit()




