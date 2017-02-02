#!/usr/bin/python3

import re
from html import unescape

# Full wattpad site -> [list of strings]
def rip_content(raw_file):
  # Convert file to list of ugly strings
  pattern = "<p data-p-id=\".{32}\">([^\n]+)</p>"
  strings = re.findall(pattern, raw_file)

  strip = lambda s: unescape(re.sub('</?[^\>]+>', '', s))
  return "\n".join([strip(line) for line in strings])

print(rip_content(open("input.txt", "r").read()))