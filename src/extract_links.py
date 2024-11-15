from textnode import (
    TextNode,
    text_type_image,
    text_type_link,
)
import re


def extract_markdown_image(text):
    url_matches = re.findall(r"\((.*?)\)", text)
    #pulls () and whatever's between them

    alt_matches = re.findall(r"\[(.*?)\]", text)
    #as above, but with []
    extracted_image = list(zip(alt_matches, url_matches))

    return extracted_image 

def extract_markdown_links(text):
    url_matches = re.findall(r"\((.*?)\)", text)
    anchor_matches = re.findall(r"\[(.*?)\]", text)

    extracted_links = list(zip(anchor_matches, url_matches))

    return extracted_links

