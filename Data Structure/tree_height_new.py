# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:   
    def __init__(self,key):
        self.key = key
        self.children = []
    def add_Children(self,child):
        self.children.append(child)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
            nodes = []
            # create nodes
            for i in range(self.n):
                nodes.append(Node(i))
            j = 0
            
            # add the children to the parent node
            for i in range(self.n):
                p_i = self.parent[i]
                if p_i == -1:
                    root = nodes[i]
                else:
                    nodes[p_i].add_Children(nodes[j])
                j+=1
            
            # compute max node searching from root
            def Height(node):
                if node is None:
                    return 0
                if len(node.children)==0:
                    return 1
                else:
                    h = []
                    for i in range(len(node.children)):
                        h.append(Height(node.children[i]))
                return 1 + max (h)
            return Height(root)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
