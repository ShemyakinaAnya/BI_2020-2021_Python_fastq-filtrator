import unittest
from unittest.mock import patch
import parser_functions
import sys


class TestInputOutputNamesParsing(unittest.TestCase):

    def setUp(self):
        self.check_input_file = parser_functions.check_input_file
        self.parse_output_base_name = parser_functions.parse_output_base_name

    def test_check_input_file_and_parse_output_base_name_no_obn_input_as_file(self):       # obn - output base name
        test_args = ['script.py', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, 'file')
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_no_obn_input_as_path(self):
        test_args = ['script.py', 'dir1/dir2/file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'dir1/dir2/file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, 'file')
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_no_obn_input_as_directory(self):
        test_args = ['script.py', 'dir1/dir/']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertIsNone(input_file)
            self.assertEqual(input_file_warning, 'Please, provide fastq input file')
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertIsNone(output_base_name)
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_no_obn_input_without_format(self):
        test_args = ['script.py', 'file']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertIsNone(input_file)
            self.assertEqual(input_file_warning, 'Please, provide fastq input file')
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertIsNone(output_base_name)
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_no_obn_no_input(self):
        test_args = ['script.py']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertIsNone(input_file)
            self.assertEqual(input_file_warning, 'Please, provide fastq input file')
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertIsNone(output_base_name)
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_obn_only_flag_input_as_file(self):
        test_args = ['script.py', '--output_base_name', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, 'file.fastq')
                self.assertEqual(output_base_name_warning, 'It is possible that you did not provide the output base '
                                                           'name. Ignore it, if your output files have the correct '
                                                           'name')

    def test_check_input_file_and_parse_output_base_name_obn_norm_input_as_file(self):
        test_args = ['script.py', '--output_base_name', 'new_name', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, 'new_name')
                self.assertIsNone(output_base_name_warning)

    def test_check_input_file_and_parse_output_base_name_obn_as_flag_input_as_file(self):
        test_args = ['script.py', '--output_base_name', '--min_length', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, '--min_length')
                self.assertEqual(output_base_name_warning, 'It is possible that you did not provide the output base '
                                                           'name. Ignore it, if your output files have the correct '
                                                           'name')

    def test_check_input_file_and_parse_output_base_name_obn_as_digit_input_as_file(self):
        test_args = ['script.py', '--output_base_name', '345', 'file.fastq']
        with patch.object(sys, 'argv', test_args):
            input_file, input_file_warning = self.check_input_file()
            self.assertEqual(input_file, 'file.fastq')
            self.assertIsNone(input_file_warning)
            if input_file:
                output_base_name, output_base_name_warning = self.parse_output_base_name(input_file)
                self.assertEqual(output_base_name, '345')
                self.assertEqual(output_base_name_warning, 'It is possible that you did not provide the output base '
                                                           'name. Ignore it, if your output files have the correct '
                                                           'name')


if __name__ == '__main__':
    unittest.main()
