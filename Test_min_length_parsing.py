import unittest
from unittest.mock import patch
import parser_functions
import sys


class TestMinLengthParsing(unittest.TestCase):

    def setUp(self):
        self.parse_min_length = parser_functions.parse_min_length

    def test_min_length_parsing_norm(self):
        test_args = ['script.py', '--min_length', '30', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            min_length, min_length_warning = self.parse_min_length()
            self.assertEqual(min_length, 30)
            self.assertIsNone(min_length_warning)

    def test_min_length_parsing_negative_value(self):
        test_args = ['script.py', '--min_length', '-30', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            min_length, min_length_warning = self.parse_min_length()
            self.assertEqual(min_length, 0)
            self.assertEqual(min_length_warning, 'Minimal length value must be greater than zero')

    def test_min_length_parsing_no_value(self):
        test_args = ['script.py', '--min_length', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            min_length, min_length_warning = self.parse_min_length()
            self.assertEqual(min_length, 0)
            self.assertEqual(min_length_warning, 'Please, provide a value for minimal length')

    def test_min_length_parsing_zero_value(self):
        test_args = ['script.py', '--min_length', '0', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            min_length, min_length_warning = self.parse_min_length()
            self.assertEqual(min_length, 0)
            self.assertIsNone(min_length_warning)

    def test_min_length_parsing_no_flag(self):
        test_args = ['script.py', '0', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            min_length, min_length_warning = self.parse_min_length()
            self.assertEqual(min_length, 0)
            self.assertIsNone(min_length_warning)


if __name__ == '__main__':
    unittest.main()
