#from argparse import ArgumentParser
import glob
import os

import random

from pprint import pprint

from config import *
from data import * 
from voting_experts import *

if __name__ == "__main__":

    files = glob.glob("data/grimm/*/*.txt")
    files = [os.path.normcase(f) for f in files]

    n_files = len(files)

    
    
    trie = build_trie(process(files[0]), 7)
    
    trie.print()
