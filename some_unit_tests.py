import os

def test_input_nonexistent_file():
    try:
        assert os.popen(r"python ./TexLinter.py C:\Users\46763\OneDrive\Skrivbord\s01\individmjukvar\ex").read() == "file not found: C:\\Users\\46763\\OneDrive\\Skrivbord\\s01\\individmjukvar\\ex\n"
    except AssertionError:
        print("failed to recognize nonexistent file")
    



def test_input_different_extension():
    try:
        os.popen(r"python ./TexLinter.py C:\Users\46763\OneDrive\Skrivbord\s01\individmjukvar\ex\test.txt").read() == "only .tex extension allowed\n"
    except AssertionError:
        print("failed to recognize different extension")



test_input_different_extension()
test_input_nonexistent_file()