import logging

class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = Node

class SLinkedList:
    def __init__(self):
        self.head = None


