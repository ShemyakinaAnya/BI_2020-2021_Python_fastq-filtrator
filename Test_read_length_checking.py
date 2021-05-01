import unittest
import filter_functions


class TestReadLengthFilter(unittest.TestCase):

    def test_filter_by_read_length(self):
        self.assertTrue(filter_functions.check_read_length(0, "asdasdasd"))
        self.assertTrue(filter_functions.check_read_length(2, "asdasdasd"))
        self.assertFalse(filter_functions.check_read_length(10, "asdasdasd"))


if __name__ == '__main__':
    unittest.main()
