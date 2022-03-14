############################################ FILE CLASS #################################################################
from Line import Line
import os


class File:
    def __init__(self, path):
        self.path = path
        self.listOfLines = []

    def check_file_existance(self):
        if(os.path.isfile(self.path)):
            return True
        else:
            print("file not found: " + self.path)
            return False

    def check_valid_file_Extension(self):
        if(self.path[-4:] == ".tex"):
            return True
        else:
            print("only .tex extension allowed")
            return False

    def getLines(self):
        file = open(self.path, "r")
        temp_list = file.readlines()
        for line in temp_list:
            self.listOfLines.append(Line(line))
        file.close()

    def analyze_Lines(self):
        for line in self.listOfLines:
            line.analyze_type()
