import logging
from hashtable import HashLogic

class Logic:
    def __init__(self):
        self.size = 50
        self.hastable = [0]*self.size

    def testdata(self):
        testString = ["abcdef", "bacdef", "cbadef", "defabc"]
        hashd = HashLogic(self.hastable, self.size)
        hashd.Insert(testString)
        hashd.PrintHashTable()

def main():
    Log = logging.getLogger('myLogger')
    Log.setLevel(20)
    logic = Logic()
    logic.testdata()

main()

