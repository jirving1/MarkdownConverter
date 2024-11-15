
import re

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            raw_line = line[2:]
            return raw_line.strip("# ")
    raise ValueError("No title found")
    