import unittest
import subprocess
import os
import filecmp


class TestFastqFilter(unittest.TestCase):

    def test_if_everything_works_together(self):
        subprocess.run(['/home/haletod/.local/share/virtualenvs/fastq_filter-fTtz5X_t/bin/python',
                        '/home/haletod/PycharmProjects/fastq_filter/fastq_filter.py',
                        '--min_length', '45', '--gc_bounds', '45', '65', '--keep_filtered', '--output_base_name',
                        'new_base_name', '/home/haletod/PycharmProjects/fastq_filter/files/final_input.fastq'])

        self.assertTrue(os.path.isfile('new_base_name__passed.fastq'))
        self.assertTrue(os.path.isfile('new_base_name__failed.fastq'))
        self.assertTrue(filecmp.cmp('new_base_name__passed.fastq', 'files/final_output__passed.fastq'))
        self.assertTrue(filecmp.cmp('new_base_name__failed.fastq', 'files/final_output__failed.fastq'))
        os.remove('new_base_name__passed.fastq')
        os.remove('new_base_name__failed.fastq')


if __name__ == '__main__':
    unittest.main()
