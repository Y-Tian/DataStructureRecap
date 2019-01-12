from collections import deque

class BSFNode(object):
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class BsfLogic(object):
    def __init__(self, graph, head, visted=set()):
        self.graph = graph
        self.head = head
        self.visited = visted

    def main(self):
        q = deque()
        s = self.head
        q.append(s)
        while q:
            currNode = q.popleft()
            print(currNode)
            if currNode not in self.visited:
                self.visited.add(currNode)
                q.append(self.graph[currNode] - self.visited)

    def printNode(self, node):
        print(node.data)


