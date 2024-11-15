import os
from markdown_blocks import markdown_to_html_node
import re

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    
    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    print(html)

    page_title = extract_title(markdown_content)
    template = template_content.replace("{{ Title }}", page_title)
    template2 = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template2)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    content_list = os.listdir(dir_path_content)
    print(f"{content_list}")
    for item in content_list:
        print(f"{item}")
        if os.path.isfile(os.path.join(dir_path_content, item)) == True:
            item_path = os.path.join(dir_path_content, item)
            dest_file = item.replace('.md', '.html')  # Change extension
            full_dest_path = os.path.join(dest_dir_path, dest_file)
            generate_page(item_path, template_path, full_dest_path)
        if os.path.isdir(os.path.join(dir_path_content, item)) == True:
            item_path = os.path.join(dir_path_content, item)
            new_directory = os.path.join(dest_dir_path, item)
            os.mkdir(new_directory)
            generate_pages_recursive(item_path, template_path, new_directory)



    
    