# TexLinter
TexLinter is developed by Ibrahim Abdulrahman.

how to start TexLinter. 
start the program by typing: python ./texlinter <name of file>

Rules are wrriten in Rules.json
NOTE!!! do not change names of variables, change only the values according to following instructions:
name of variable in json file: True/F 
	"add_space_after_comment" : "True/False",
	"add_blank_line_after_section" : "1-9",
	"add_new_line_after_sentece" : "True/False",
	"sort_packages" : "True/False",
	"indentation" : "Tabs/Spaces"

NOTE!!! 
- please notice upper and lower case for letters in value.
- If Value is not wrriten correctly the Linter will ignore executing the rule.
- TexLinter accepts only (.tex) extenstion. 
- Make sure to input right file name. 

The formatted file is placed in same folder of orginal file. 
