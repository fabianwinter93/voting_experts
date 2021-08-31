import numpy as np

from config import *

class Node(object):
    def __init__(self, data, is_root=False):
        self.data = data
        self.children = {}
        self.is_root = is_root
        self.freq = 0



class Trie(object):
    def __init__(self):
        self.root = Node("", is_root=True)

    def add_seq(self, seq):
        node = self.root

        for c in seq:
            node.children.setdefault(c, Node(c))
            node = node.children[c]
            node.freq += 1

    def print(self):
        
        def rec_print(node, depth,prefix):
            print("---"*(depth+1), prefix, repr(node.data), node.freq)
            for k, c in node.children.items():
                rec_print(c, depth+1, prefix+node.data)
            if node.is_root is False and len(node.children) == 0:
                input()

        rec_print(self.root, 0, "")



def build_trie(sequence, n):

    ngrams = [sequence[i:i+n] for i in range(len(sequence)-n+1)]
    #print(ngrams)

    trie = Trie()

    for gram in ngrams:
        trie.add_seq(gram)

    return trie