#!/usr/bin/env python

import sys

# refs: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
# TODO
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def initRules():
    pass

def parseLine(line):
    words = [line]
    return words

def decorate(word):
    # TODO
    return bcolors.OKGREEN + word + bcolors.ENDC

def colorize(line):
    words = parseLine(line)
    return ''.join([decorate(word) for word in words])

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for line in lines:
        print colorize(line.strip())
