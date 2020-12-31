import json


with open('example.json') as f:
    array = json.load(f)


# print(array['graph']['nodes'][2])


class Node:
    def init(self, name):
        self.children = []
        self.name = name
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue)> 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


