# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Utility functions for the program

import os
import codecs
import sys

def removeNewLine(string):
    # If string has new line at the end, remove it
    if (string[-1] == '\n'):
        return string[:-1]
    return string

def removeSpaces(string):
    # Remove any spaces from start and back
    return string.strip()

def removeUnwantedChars(string):
    return removeSpaces(removeNewLine(string))