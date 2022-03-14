############################################ Linter CLASS #################################################################
import json
import sys
import re
import os 
from Line import Line
from File import File


class Linter:
    def __init__(self, file=None):
        self.file = file
        self.rules = None

    def get_rules_from_Json(self):
        # get rules from json file,  no exception handling here
        if  os.path.isfile("Rules.json"):
            with open("Rules.json") as jsonFile:
                data = json.load(jsonFile)
            jsonFile.close()
            self.rules = data
            return True
        else:
            print("Rules file not found: Rules.json")
            return False

    def get_Input_Terminal(self):
        try:
            inp_1 = sys.argv[1]
            return inp_1
        except IndexError:
            print("please enter the name of wanted file")
            return False

    def add_space_after_comment(self):
        try:
            val = self.rules['add_space_after_comment']
            expr = re.compile(r'%[^%\s]|[^%\s]%')
            if val == "True":
                for line in self.file.listOfLines:
                    cond = True
                    while cond:
                        if expr.search(line.text) is not None:
                            ind = expr.search(line.text).span()[0]
                            line.text = line.text[:ind+1] + \
                                " " + line.text[ind+1:]
                        else:
                            cond = False

        except KeyError:
            print(
                "Please Don't change variable name in JSON file: add_space_after_comment")

    def add_blank_line_before_section(self):
        try:
            val = int(self.rules["add_blank_line_after_section"])
            list_of_sec_words = ["\part", "\chapter", "\section",
                                 "\subsection", "\subsubsection", "\paragraph", "\subparagraph"]
            list_of_index = []
            if val > 0:
                # finding index of sections in the file
                for index, line in enumerate(self.file.listOfLines):
                    if line.text_type in list_of_sec_words:
                        list_of_index.append(index)

                new_Line = Line("\n")
                new_Line.text_type = "\n"

                # inserting new line before sections and recalculate next index value after adding (val) of new lines
                for i, index in enumerate(list_of_index):
                    index = index + i*val
                    for i in range(val):
                        self.file.listOfLines.insert(index, new_Line)
        except KeyError:
            print(
                "Please Don't change variable name in JSON file: add_blank_line_after_section.")
        except ValueError:
            print("Make sure you enterd valid value in (add_blank_line_after_section) in JSON file, only numbers are accepted")

    def add_newLine_after_end_of_sentence(self):
        try:
            val = self.rules["add_new_line_after_sentece"]
            if val == "True":
                expr = re.compile(r'\.[A-Z]|\.\s*[A-Z]')

                for index, line in enumerate(self.file.listOfLines):
                    if line.text_type == "text":
                        if expr.search(line.text) is not None:
                            index_of_point = expr.search(
                                line.text).span()[1] - 1
                            text_line = Line(line.text[index_of_point:])
                            text_line.text_type = "text"
                            self.file.listOfLines.insert(index + 1, text_line)
                            line.text = line.text[:index_of_point] + "\n"
        except KeyError:
            print(
                "Please Don't change variable name in JSON file: add_new_line_after_sentece")

    # sorting packages and keeping them in same lines but with different ording.
    def sort_packages(self):
        try:
            val = self.rules["sort_packages"]
            if val == "True":
                expr = re.compile(r'\{\s*\w{,}\s*}')
                packagesName = []
                line_indexs = []
                lineText = []
                for index, line in enumerate(self.file.listOfLines):
                    if line.text_type == "\\usepackage":
                        if expr.search(line.text) is not None:
                            packagesName.append(line.text[expr.search(line.text).span()[0]:expr.search(
                                line.text).span()[1]].replace(" ", "").replace("{", "").replace("}", ""))
                            line_indexs.append(index)

                zipped_list = zip(packagesName, line_indexs)
                sorted_pair = sorted(zipped_list)

                for package in sorted_pair:
                    lineText.append(self.file.listOfLines[package[1]])

                cnt = 0
                for line in lineText:
                    self.file.listOfLines[line_indexs[cnt]] = line
                    cnt += 1

        except KeyError:
            print("Please Don't change variable name in JSON file: sort_packages")

    def indent_blocks(self):
        try:
            val = self.rules["indentation"]
            indentation = ""
            if val == "Tabs":
                indentation = "\t"
            elif val == "Spaces":
                indentation = "   "
            cntr = 0
            for line in self.file.listOfLines:
                if line.text_type == "\\begin":
                    line.text = indentation*cntr + line.text
                    cntr += 1
                    continue
                elif line.text_type == "\\end":
                    cntr -= 1
                line.text = indentation*cntr + line.text
        except KeyError:
            print("Please Don't change variable name in JSON file: indentation")

    def print_file(self):
        with open(self.file.path[:-4] + "formatted.tex", "w") as fi:
            for line in self.file.listOfLines:
                fi.write(line.text)
            fi.close()
