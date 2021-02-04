import sys

# Parsing
min_length = 0
keep_filtered = False
gc_bounds = [0, 100]
output_base_name = None
input_file = sys.argv[-1]
for ind, arg in enumerate(sys.argv):
    if arg == '--min_length':
        try:
            min_length = int(sys.argv[ind + 1])
            if int(sys.argv[ind + 1]) < 0:
                min_length = 0
                print('Minimal length value must be greater than zero')
        except ValueError:
            print('Please, provide a value for minimal length')
    elif arg == '--keep_filtered':
        keep_filtered = True
    elif arg == '--gc_bounds':
        try:
            gc_bounds[0] = int(sys.argv[ind + 1])
            if 0 < gc_bounds[0] < 100:
                if sys.argv[ind + 2].isdigit():
                    if gc_bounds[0] < int(sys.argv[ind + 2]) < 100:
                        gc_bounds[1] = int(sys.argv[ind + 2])
                    else:
                        gc_bounds[1] = 100
                        print('Value of the upper bound of GC content must be between lower bound and 100')
            else:
                gc_bounds[0] = 0
                print('Value of the lower bound of GC content must be between 0 and 100')
        except ValueError:
            print('Please, provide at least one value for GC content')
    elif arg == '--output_base_name':
        output_base_name = sys.argv[ind + 1]

if output_base_name is None:
    output_base_name = input_file[:-len(".fastq")]


# fastq_filter programm
def check_read_length(min_length, seq_read):
    return min_length is None or len(seq_read) >= min_length


def check_read_gc(gc_bound_min, gc_bound_max, seq_read):
    if gc_bound_min is None:
        return True

    GC_counts = 0
    for chr in seq_read:
        if chr == 'G' or chr == 'g' or chr == 'C' or chr == 'c':
            GC_counts += 1
    GC_content = int(GC_counts / len(seq_read) * 100)

    if gc_bound_max is None:
        return GC_content >= gc_bound_min
    else:
        return gc_bound_min <= GC_content <= gc_bound_max

output_file_passed_name = output_base_name + '__passed.fastq'
output_file_failed_name = output_base_name + '__failed.fastq'

with open(input_file) as fastq_file, open(output_file_passed_name, 'w') as p:
    if keep_filtered:
        f = open(output_file_failed_name, 'w')

    string_1 = fastq_file.readline()
    while string_1:
        string_2 = fastq_file.readline()
        string_3 = fastq_file.readline()
        string_4 = fastq_file.readline()
        read = string_1 + string_2 + string_3 + string_4

        read_is_good = check_read_length(min_length, string_2) and check_read_gc(gc_bounds[0], gc_bounds[1], string_2)
        if read_is_good:
            p.write(read)
        else:
            if keep_filtered:
                f.write(read)

        string_1 = fastq_file.readline()
    if keep_filtered:
        f.close()