import logging

class SLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        currNode = self.head
        while currNode is not None:
            logging.info(currNode.data)
            print(currNode.data)
            currNode = currNode.nextNode

    def getSize(self):
        size = 0
        currNode = self.head
        while currNode is not None:
            size += 1
            currNode = currNode.nextNode
        return size

    def appendNode(self, data):
        head = self.head
        newNode = SLinkedListNode(data)
        head.nextNode = newNode
    
    def pushNode(self, data):
        tempNode = self.head
        newNode = SLinkedListNode(data)
        self.head = newNode
        self.head.nextNode = tempNode

    def insertNode(self, data, index):
        if index <= self.getSize():
            newNode = SLinkedListNode(data)
            currNode = self.head
            for i in range(0, index-1):
                currNode = currNode.nextNode
            tempNode = currNode.nextNode
            currNode.nextNode = newNode
            currNode = currNode.nextNode
            currNode.nextNode = tempNode
    
    def removeNode(self, index):
        if index <= self.getSize():
            currNode = self.head
            for i in range(0, index-1):
                currNode = currNode.nextNode
            currNode.nextNode = currNode.nextNode.nextNode
