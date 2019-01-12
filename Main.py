import logging
from hashing.hashtable import HashLogic
from linkedlists.singlylinkedlist import SLinkedList
from bfs.bfs import BsfLogic
from linkedlists.singlylinkedlist import SLinkedListNode
from bfs.bfs import BSFNode

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
        nodeHead = SLinkedListNode("0")
        linkedlist = SLinkedList()
        linkedlist.head = nodeHead
        linkedlist.appendNode("5")
        linkedlist.insertNode("6", 1)
        linkedlist.removeNode(2)
        linkedlist.pushNode("2")
        linkedlist.traverse()

    def testBsfData(self):
        nodeA = BSFNode("1")
        nodeB = BSFNode("2")
        nodeC = BSFNode("3")
        nodeD = BSFNode("4")
        nodeE = BSFNode("5")
        nodeF = BSFNode("6")
        nodeG = BSFNode("7")
        graph = {nodeA : set([nodeB, nodeC]),
                 nodeB : set([nodeD, nodeE]),
                 nodeC : set([nodeF, nodeG])}
        graphHashable = {'A' : set(['B', 'C']),
                         'B' : set(['D', 'E']),
                         'C' : set(['F', 'G'])}
        bsf = BsfLogic(graphHashable, 'A')
        bsf.main()

def main():
    Log = logging.getLogger('myLogger')
    Log.setLevel(20)
    logic = Logic()
    # logic.testHashData()
    # logic.testSLinkedListData()
    logic.testBsfData()

main()

