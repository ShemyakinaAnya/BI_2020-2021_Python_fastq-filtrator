# BI_2020-2021_Python_fastq-filtrator

Filter of sequences in FASTQ format with thresholds for sequence length
and its GC content

The options for the tool are as follows:

--min_length            Provide a positive integer specifying the lower
                        threshold for filtering reads by length.
                        Default minimal length is 0 if not specified.

--gc_bounds             Provide one or two positive integers between 0 and 100
                        specifying lower or lower and upper bounds for
                        filtering reads by GC content percent. If not specified
                        the default values are set as 0 and 100, correspondingly.

--keep_filtered         If this flag is present then the reads that failed
                        filtration will be written/collected in separate output
                        file.

--output_base_name      Provide a base name (filename without extension) for
                        output files. If not specified the default base name
                        will be set as non-extension part of the input
                        filename. The name of output file with filtered reads
                        will consist of base name, ‘__passed’ suffix and format
                        extension (‘.fastq’). If --keep_filtered is set,
                        the second output file name will consist of base name,
                        ‘__failed’ suffix and format extension.

path to FASTQ file      A required positional argument, providing path to the
                        input file; should be entered as the last one.

All options except the path to input file are optional

