#!/usr/bin/env python

import sys
import re

# refs: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
# TODO more better definition
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

def parseLine(line):
    words = [line]
    return words

def decorateNumber(match):
    # TODO configurable
    # rules = [
    #         {'warn': {'number': {'gt': 99}}},
    #         ]
    # for rule in rules:
    #     (level, expression) = rule.items()[0]
    #     if level == 'warn':
    #         pass

    number = float(match.group(0))
    color = ''
    if 200 < number:
        color = bcolors.FAIL
    elif 100 <= number < 200:
        color = bcolors.WARNING
    else:
        color = bcolors.OKGREEN

    if color:
        return color + str(number) + bcolors.ENDC
    return str(number)

def decorate(line):
    # TODO can decorate specified string
    decorated = re.sub(r'(\d+(\.\d+)?)', decorateNumber, line)
    return decorated

def colorize(line):
    return decorate(line)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for line in lines:
        print colorize(line.strip())
