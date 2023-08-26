import re


def regexFunction(r, inputList):
    new = re.compile(r)
    newList = list(filter(new.match, inputList))
    return newList

