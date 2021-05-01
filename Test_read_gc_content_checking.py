import unittest
import filter_functions


class TestReadGCContentFilter(unittest.TestCase):

    def test_check_read_gc(self):
        self.assertTrue(filter_functions.check_read_gc(5, 40, "tcfagggccuieljso"))
        self.assertFalse(filter_functions.check_read_gc(5, 40, "tcfagggccuieljsoggggggggggggggggg"))
        self.assertTrue(filter_functions.check_read_gc(0, 100, " "))


if __name__ == '__main__':
    unittest.main()
