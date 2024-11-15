import unittest
from extract_title import extract_title

class ExtractTitleTests(unittest.TestCase):
    def test_simple_title(self):
        markdown = "# This is a Title"
        title = extract_title(markdown)
        self.assertEqual("This is a Title", title)

    def test_multiple_headings(self):
        markdown = """# This is a title
                ## This is an h2
                ### this is an h3"""
        title = extract_title(markdown)
        self.assertEqual("This is a title", title)
    
    def test_complex_markdown(self):
        markdown = """# This is a title
            > this is a block quote
            ``` this is a code block```
            - this is an unordered list
            - this is also an unordered list
            1. this is an ordered list
            2. this is also an ordered list
            ## This is an h2
            this is a paragrpah
             this is also a paragraph """
        title = extract_title(markdown)
        self.assertEqual("This is a title", title)

if __name__ == "__main__":
    unittest.main()

