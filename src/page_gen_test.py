import unittest

from generate_page import extract_title

class ExtractTitle(unittest.TestCase):
    def test_eq(self):
        md = "# This is a title"
        title = extract_title(md)
        self.assertEqual("This is a title", title)
    
    def test_eq_double(self): 
        actual = extract_title("""# This is a title
                               # This is a second title that should be ignored""")
        self.assertEqual("This is a title", actual)
    
    def test_eq_h2_start(self):
        actual = extract_title("""## this is a false flag
                               # This is a title
                               # this is a second title
                               ### this is a test h3""")
        self.assertEqual("This is a title", actual)


if __name__ == "__main__":
    unittest.main()
        