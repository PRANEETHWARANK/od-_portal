import re
import os

filepath = r'e:\AMRITA_OD_PORTAL\templates\od\apply_od.html'
if not os.path.exists(filepath):
    print(f"File not found: {filepath}")
    exit(1)

with open(filepath, 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    tags = re.findall(r'\{%\s*(.*?)\s*%\}', line)
    for tag in tags:
        print(f"Line {i+1}: {tag}")
