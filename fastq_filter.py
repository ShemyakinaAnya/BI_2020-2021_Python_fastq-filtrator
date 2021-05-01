import sys
import filter_functions
import parser_functions


call_help = parser_functions.parse_call_help()
if not call_help:
    input_file, input_file_warning = parser_functions.check_input_file()
    if not input_file_warning:

        min_length, min_length_warning = parser_functions.parse_min_length()
        gc_bounds, gc_bounds_warning = parser_functions.parse_gc_bounds()
        output_base_name, output_base_name_warning = parser_functions.parse_output_base_name(input_file)
        keep_filtered = parser_functions.parse_keep_filtered()

        if min_length_warning is not None:
            print(min_length_warning)
        if gc_bounds_warning is not None:
            print(gc_bounds_warning)
        if output_base_name_warning is not None:
            print(output_base_name_warning)

        filter_functions.filter_file(input_file, min_length, gc_bounds, output_base_name, keep_filtered)

    else:
        print(input_file_warning)
else:
    print(parser_functions.help_note)
