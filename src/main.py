
from copy_static import copy_static
import os
from generate_page import generate_pages_recursive 

def main():
    source_directory = './static'
    destination_directory = 'public'
    copy_static(source_directory, destination_directory)

    from_path = "./content"
    template_path = "./template.html"
    dest_path = "./public"
    
    generate_pages_recursive(from_path, template_path, dest_path)

    
main()

