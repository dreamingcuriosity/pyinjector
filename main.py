from imports import *
from jinja2 import Template
import sys

if len(sys.argv) < 3:
    print("usage: python main.py <TEMPLATE_FILE> <OUTPUT_FILE>")
    sys.exit(1)

template_file = sys.argv[1]
output_file = sys.argv[2]

# Read the template
with open(template_file, "r") as f:
    template_content = f.read()

params = {}
with open("vars", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            params[key] = value
        else:
            print(f"Skipping invalid parameter '{line}'")
# Render template with dynamic parameters
template = Template(template_content)
rendered = template.render(**params)

# Write output
with open(output_file, "w") as f:
    f.write(rendered)

print(f"Rendered template saved to {output_file}")

