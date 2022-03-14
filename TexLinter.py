################################################### Main function #############################################################
from File import File
from Linter import Linter


def main():
    linter = Linter()
    path = linter.get_Input_Terminal()
    file = File("")
    if path:
        file = File(path) 
        file_check = file.check_file_existance() and file.check_valid_file_Extension() and linter.get_rules_from_Json()
        if file_check:
            linter.file = file
            linter.file.getLines()
            linter.file.analyze_Lines()
            linter.add_space_after_comment()
            linter.add_blank_line_before_section()
            linter.add_newLine_after_end_of_sentence()
            linter.sort_packages()
            linter.indent_blocks()
            linter.print_file()
            print("done!")
            

main()


