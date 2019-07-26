import os
import re
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIR = os.environ.pop("INIT_CONFIG_TEMPLATE_DIR", "/templates")
OUTPUT_DIR = os.environ.pop("INIT_CONFIG_DATA_DIR", "/config")

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(["html", "xml"])
)

with open(os.path.join(OUTPUT_DIR, "env"), "w") as ofile:
    ofile.write(str(os.environ))

for file_name in os.listdir(TEMPLATE_DIR):
    if not file_name.endswith(".jinja2"):
        shutil.copy(os.path.join(TEMPLATE_DIR, file_name), os.path.join(OUTPUT_DIR, file_name))

for template_name in env.list_templates(extensions=["jinja2"]):
    template = env.get_template(template_name)
    with open(os.path.join(OUTPUT_DIR, re.sub("\.jinja2$", "", template.name)), "w") as ofile:
        ofile.write(template.render(**os.environ))
