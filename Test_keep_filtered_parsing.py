import unittest
from unittest.mock import patch
import parser_functions
import sys


class TestKeepFilteredParsing(unittest.TestCase):

    def setUp(self):
        self.parse_keep_filtered = parser_functions.parse_keep_filtered

    def test_parse_keep_filtered(self):
        test_args = ['script.py', '--keep_filtered', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            keep_filtered = self.parse_keep_filtered()
            self.assertTrue(keep_filtered)

    def test_parse_keep_filtered_exception(self):
        test_args = ['script.py', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            keep_filtered = self.parse_keep_filtered()
            self.assertFalse(keep_filtered)


if __name__ == '__main__':
    unittest.main()
