# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Reads file
import sys

from utils import removeUnwantedChars
from readFile import readInput

from textPrinted.main import TERMINAL_OR_LOG, INCORRECT_OUTPUT_STYLE

INPUT_FILE = './testFile/test.txt'
OUTPUT_FILE = "output.txt"

if __name__ == '__main__':
    # Read the input file for list of restaurants and scores
    lines = readInput(INPUT_FILE)

    # Output file or terminal
    outputStyle = input(TERMINAL_OR_LOG)

    # Log file
    if (outputStyle == "1"):
        original_stdout = sys.stdout
        fptr = open(OUTPUT_FILE, 'w')
        sys.stdout = fptr    

        for line in lines:
            fptr.write(removeUnwantedChars(line) + "\n")
    
        sys.stdout = original_stdout
        fptr.close()

    # Terminal
    elif (outputStyle == "2"):
        for line in lines:
            print(removeUnwantedChars(line))

    # Neither 1 or 2
    else:
        print(INCORRECT_OUTPUT_STYLE)