import re
import os

filepath = r'e:\AMRITA_OD_PORTAL\templates\od\apply_od.html'
with open(filepath, 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line_num = i + 1
    # Match any {% ... %} tag
    matches = re.finditer(r'\{%\s*(.*?)\s*%\}', line)
    for match in matches:
        tag_content = match.group(1).split()[0] # Get the first word of the tag
        print(f"L{line_num}: {tag_content}")
