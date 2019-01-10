import logging

class HashLogic(object):
    def __init__(self, table, size):
        self.table = table
        self.size = size

    def HashFuncString(self, string):
        # order does matter
        asciiTemp = 0
        index = 1
        for char in string:
            sum = ord(char)
            asciiTemp += sum*10+index
            index += 1
        return asciiTemp%2069

    def Search(self, key):
        if key:
            return self.table[key]

    def Insert(self, obj):
        if isinstance(obj, str):
            key = self.HashFuncString(obj)
            logging.info(key)
        if key:
            self.table[key] = obj