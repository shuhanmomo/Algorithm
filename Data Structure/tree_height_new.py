# python3
# Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
# that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
# leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

# Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
# from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
# otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
# It is guaranteed that the input represents a tree.

# Constraints. 1 ≤ 𝑛 ≤ 105.

# Output Format. Output the height of the tree.
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
