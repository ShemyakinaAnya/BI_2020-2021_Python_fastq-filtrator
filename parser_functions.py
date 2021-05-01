import sys


help_note = 'Filter of sequences in FASTQ format with thresholds for sequence length and its GC content\n\nThe' \
            ' options for the tool are as follows:\n\n--min_length\t\tProvide a positive integer specifying the lower' \
            ' threshold for filtering reads\n\t\t\tby length. Default minimal length is 0 if not specified.\n\n' \
            '--gc_bounds\t\tProvide one or two positive integers between 0 and 100 specifying lower or lower and' \
            '\n\t\t\tupper bounds for filtering reads by GC content percent. If not specified the default\n\t\t\t' \
            'values are set as 0 and 100, correspondingly.\n\n--keep_filtered\t\tIf this flag is present then the' \
            ' reads that failed filtration will be collected\n\t\t\tin separate output file.\n\n--output_base_name\t' \
            'Provide a base name (filename without extension) for output files. If not specified\n\t\t\tthe default' \
            ' base name will be set as non-extension part of the input filename.\n\t\t\tThe name of output file with' \
            ' filtered reads will consist of base name, ‘__passed’\n\t\t\tsuffix and format extension (‘.fastq’). ' \
            'If --keep_filtered is set, the second output\n\t\t\tfile name will consist of base name, ‘__failed’ ' \
            'suffix and format extension.\n\npath to FASTQ file\tA required positional argument, providing path to' \
            ' the input file;\n\t\t\tshould be entered as the last one.\n\n--help\t\t\tPrints this help note and' \
            ' exits.\n\nAll options except the path to input file are optional'


def check_input_file():
    warning = None
    input_file = None
    path = sys.argv[-1].split('/')
    if ".fastq" in path[-1]:
        input_file = sys.argv[-1]
    else:
        warning = 'Please, provide fastq input file'
    return input_file, warning


def parse_min_length():
    warning = None
    value = 0
    if '--min_length' in sys.argv:
        flag_index = sys.argv.index('--min_length')
        value = sys.argv[flag_index + 1]
        try:
            value = int(value)
            if value < 0:
                value = 0
                warning = 'Minimal length value must be greater than zero'
        except ValueError:
            value = 0
            warning = 'Please, provide a value for minimal length'
    return value, warning


def parse_gc_bounds():
    warning = None
    values = [0, 100]
    if '--gc_bounds' in sys.argv:
        flag_index = sys.argv.index('--gc_bounds')
        values[0] = sys.argv[flag_index + 1]
        try:
            values[0] = int(values[0])
            if 0 < values[0] < 100:
                possible_max_value = sys.argv[flag_index + 2]
                try:
                    possible_max_value = int(possible_max_value)
                    if values[0] < possible_max_value < 100:
                        values[1] = possible_max_value
                    else:
                        warning = 'Value of the upper bound of GC content must be between lower bound and 100'
                except ValueError:
                    pass
            else:
                values[0] = 0
                warning = 'Value of the lower bound of GC content must be between 0 and 100'
        except ValueError:
            values[0] = 0
            warning = 'Please, provide at least one value for GC content'
    return values, warning


def parse_output_base_name(input_file):
    path = input_file.split('/')
    name = path[-1][:-len(".fastq")]
    warning = None
    possible_wrong_names = ['--min_length', '--gc_bounds', '--keep_filtered', '--help', '--output_base_name', path[-1]]
    if '--output_base_name' in sys.argv:
        flag_index = sys.argv.index('--output_base_name')
        name = sys.argv[flag_index + 1]
        if name in possible_wrong_names or name.isdigit():
            warning = 'It is possible that you did not provide the output base name. Ignore it, if your output files' \
                      ' have the correct name'
    return name, warning


def parse_keep_filtered():
    if '--keep_filtered' in sys.argv:
        return True
    else:
        return False


def parse_call_help():
    if '--help' in sys.argv:
        return True
    else:
        return False
