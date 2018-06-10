#!/usr/local/bin/python3
# Code for: Python Challenge 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request
import re

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as response:
   html = str(response.read())

working = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
match = ''.join(re.findall('..(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])..', working))

print(match)

# Answer: linkedlist
