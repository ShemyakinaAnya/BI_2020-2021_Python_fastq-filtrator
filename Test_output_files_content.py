import unittest
import filter_functions
import os
import filecmp


class TestOutputFilesContent(unittest.TestCase):

    def test_check_output_files(self):
        # check filtration by min_length and keep-filtered
        filter_functions.filter_file('files/input1.fastq', 55, [0, 100], 'result1', True)
        self.assertTrue(os.path.isfile('result1__passed.fastq'))
        self.assertTrue(os.path.isfile('result1__failed.fastq'))
        self.assertTrue(filecmp.cmp('result1__passed.fastq', 'files/result1__passed.fastq'))
        self.assertTrue(filecmp.cmp('result1__failed.fastq', 'files/result1__failed.fastq'))
        os.remove('result1__passed.fastq')
        os.remove('result1__failed.fastq')

        # check filtration by gc content and keep-filtered
        filter_functions.filter_file('files/input2.fastq', 10, [45, 55], 'result2', True)
        self.assertTrue(os.path.isfile('result2__passed.fastq'))
        self.assertTrue(os.path.isfile('result2__failed.fastq'))
        self.assertTrue(filecmp.cmp('result2__passed.fastq', 'files/result2__passed.fastq'))
        self.assertTrue(filecmp.cmp('result2__failed.fastq', 'files/result2__failed.fastq'))
        os.remove('result2__passed.fastq')
        os.remove('result2__failed.fastq')

        # check filtration by gc content and keep-filtered
        filter_functions.filter_file('files/input2.fastq', 10, [45, 55], 'result3', False)
        self.assertTrue(os.path.isfile('result3__passed.fastq'))
        self.assertFalse(os.path.isfile('result3__failed.fastq'))
        self.assertTrue(filecmp.cmp('result3__passed.fastq', 'files/result3__passed.fastq'))
        os.remove('result3__passed.fastq')


if __name__ == '__main__':
    unittest.main()