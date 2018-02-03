import unittest
import functools
from after_torrents_clean_up import *

print_header = True
header = "\n\n\nStarting Test suite execution:"


def PrintTestName(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        global print_header
        if print_header:
            print header
            print_header = False
        print('Running Unit Test TC: {}'.format(f.__name__))
        return f(*args, **kwargs)
    return wrapped


class UtCheckFileExtention(unittest.TestCase):

    @PrintTestName
    def test01_emptyFileName(self):
        self.assertRaises(ValueError, check_file_extention, "", extentions_subs)

    @PrintTestName
    def test02_emptyExtentionList(self):
        self.assertRaises(ValueError, check_file_extention, "textFileName", [])

    @PrintTestName
    def test03_emptyExtentionNotList(self):
        self.assertRaises(ValueError, check_file_extention, "textFileName", "testStringInsteadOFList")

    @PrintTestName
    def test04_fileName_Allowed_Extention(self):
        self.assertTrue(check_file_extention("movie.sub", extentions_subs))

    @PrintTestName
    def test05_fileName_Forbidden_Extention(self):
        self.assertFalse(check_file_extention("movie.txt", extentions_subs))

    @PrintTestName
    def test05_fileName_No_Extention(self):
        self.assertFalse(check_file_extention("movie", extentions_subs))


if __name__ == '__main__':
    unittest.main()
