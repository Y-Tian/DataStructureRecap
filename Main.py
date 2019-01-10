import logging
from hashing.hashtable import HashLogic
from linkedlists.singlylinkedlist import SLinkedList
from linkedlists.singlylinkedlist import Node

class Logic:
    def __init__(self):
        self.size = 50
        self.hastable = [0]*self.size

    def testHashData(self):
        testString = ["abcdef", "bacdef", "cbadef", "defabc"]
        hashd = HashLogic(self.hastable, self.size)
        hashd.Insert(testString)
        hashd.PrintHashTable()

    def testSLinkedListData(self):
        nodeHead = Node("0")
        linkedlist = SLinkedList()
        linkedlist.head = nodeHead
        linkedlist.appendNode("5")
        linkedlist.insertNode("6", 1)
        linkedlist.removeNode(2)
        linkedlist.pushNode("2")
        linkedlist.traverse()

def main():
    Log = logging.getLogger('myLogger')
    Log.setLevel(20)
    logic = Logic()
    # logic.testHashData()
    logic.testSLinkedListData()

main()

