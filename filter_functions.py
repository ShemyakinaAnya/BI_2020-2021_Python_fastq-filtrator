def check_read_length(min_length, seq_read):
    return min_length == 0 or len(seq_read) >= min_length


def check_read_gc(gc_bound_min, gc_bound_max, seq_read):
    if gc_bound_min == 0:
        return True

    GC_counts = 0
    for chr in seq_read:
        if chr == 'G' or chr == 'g' or chr == 'C' or chr == 'c':
            GC_counts += 1
    GC_content = int(GC_counts / len(seq_read) * 100)

    if gc_bound_max == 100:
        return GC_content >= gc_bound_min
    else:
        return gc_bound_min <= GC_content <= gc_bound_max


def filter_file(input_file, min_length, gc_bounds, output_base_name, keep_filtered):
    if output_base_name is None:
        output_base_name = input_file[:-len(".fastq")]

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

            read_is_good = check_read_length(min_length, string_2) and check_read_gc(gc_bounds[0], gc_bounds[1],
                                                                                     string_2)
            if read_is_good:
                p.write(read)
            else:
                if keep_filtered:
                    f.write(read)

            string_1 = fastq_file.readline()
        if keep_filtered:
            f.close()
