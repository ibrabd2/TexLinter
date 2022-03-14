############################################ LINE CLASS #################################################################
import re


class Line:
    def __init__(self, text):
        self.text = text
        self.text_splitted = text.split()
        self.text_type = None

    def analyze_type(self):
        if len(self.text_splitted) == 0:
            self.text_type = "\n"
        elif self.text_splitted[0][0].isalpha():
            self.text_type = "text"

        else:
            expr = re.compile(r'^\\\w{,}')
            if expr.search(self.text_splitted[0]) is not None:
                self.text_type = self.text_splitted[0][expr.search(self.text_splitted[0]).span()[
                    0]:expr.search(self.text_splitted[0]).span()[1]]
            else:
                if self.text_splitted[0][0] == "%":
                    self.text_type = "%"
