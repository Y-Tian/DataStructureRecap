import logging
from hashtable import HashLogic

class Logic:
    def __init__(self):
        self.size = 5000
        self.hastable = [None]*self.size

    def testdata(self):
        testString = "abcdef"
        logging.info(testString)
        hashd = HashLogic(self.hastable, self.size)
        hashd.Insert(testString)

def main():
    print("hi")
    logic = Logic()
    logic.testdata()

