import unittest
from unittest.mock import patch
import parser_functions
import sys


class TestGCBoundsParsing(unittest.TestCase):

    def setUp(self):
        self.parse_gc_bounds = parser_functions.parse_gc_bounds

    def test_gc_bounds_parsing_norm(self):
        test_args = ['script.py', '--gc_bounds', '30', '70', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [30, 70])
            self.assertIsNone(gc_bounds_warning)

    def test_gc_bounds_parsing_upper_above_100(self):
        test_args = ['script.py', '--gc_bounds', '30', '170', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [30, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the upper bound of GC content must be between lower bound '
                                                'and 100')

    def test_gc_bounds_parsing_upper_below_lower(self):
        test_args = ['script.py', '--gc_bounds', '30', '23', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [30, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the upper bound of GC content must be between lower bound '
                                                'and 100')

    def test_gc_bounds_parsing_upper_negative(self):
        test_args = ['script.py', '--gc_bounds', '30', '-23', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [30, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the upper bound of GC content must be between lower bound '
                                                'and 100')

    def test_gc_bounds_parsing_both_negative_upper_above_lower(self):
        test_args = ['script.py', '--gc_bounds', '-30', '-13', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the lower bound of GC content must be between 0 and 100')

    def test_gc_bounds_parsing_both_negative_upper_below_lower(self):
        test_args = ['script.py', '--gc_bounds', '-30', '-43', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the lower bound of GC content must be between 0 and 100')

    def test_gc_bounds_parsing_one_value(self):
        test_args = ['script.py', '--gc_bounds', '5', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [5, 100])
            self.assertIsNone(gc_bounds_warning)

    def test_gc_bounds_parsing_one_negative_value(self):
        test_args = ['script.py', '--gc_bounds', '-30', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the lower bound of GC content must be between 0 and 100')

    def test_gc_bounds_parsing_one_value_zero(self):
        test_args = ['script.py', '--gc_bounds', '0', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertEqual(gc_bounds_warning, 'Value of the lower bound of GC content must be between 0 and 100')

    def test_gc_bounds_parsing_no_value(self):
        test_args = ['script.py', '--gc_bounds', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertEqual(gc_bounds_warning, 'Please, provide at least one value for GC content')

    def test_gc_bounds_parsing_no_flag(self):
        test_args = ['script.py', '7', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            gc_bounds, gc_bounds_warning = self.parse_gc_bounds()
            self.assertEqual(gc_bounds, [0, 100])
            self.assertIsNone(gc_bounds_warning)


if __name__ == '__main__':
    unittest.main()
