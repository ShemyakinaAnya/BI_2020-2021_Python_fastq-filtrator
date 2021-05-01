import unittest
from unittest.mock import patch
import parser_functions
import sys


class TestCallHelpParsing(unittest.TestCase):

    def setUp(self):
        self.parse_call_help = parser_functions.parse_call_help

    def test_parse_call_help(self):
        test_args = ['script.py', '--help']
        with patch.object(sys, 'argv', test_args):
            call_help = self.parse_call_help()
            self.assertTrue(call_help)

    def test_parse_call_help_exception(self):
        test_args = ['script.py']
        with patch.object(sys, 'argv', test_args):
            call_help = self.parse_call_help()
            self.assertFalse(call_help)


if __name__ == '__main__':
    unittest.main()
