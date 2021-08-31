# data

import glob
import unicodedata
from unidecode import unidecode
import string

from config import * 


def fopen(path):
    return open(path, encoding=file_encoding)

def clean(text):
    text = unicodedata.normalize(unicode_norm, text)
    
    if clean_keep:
        keeps = {c:unidecode(c) for c in "äöüÄÖÜ"}

        for c, rep in keeps.items():
            text = text.replace(c, "#replace"+rep+"replace#")
        
        text = unidecode(text)

        for c, rep in keeps.items():
            text = text.replace("#replace"+rep+"replace#", c) 
    else:
        text = unidecode.unidecode(text)

    if clean_lower:
        text = text.lower()

    text = text.strip()
    return text

def tokenize(text):
    return list(text)

def process(path):
    return tokenize(clean(fopen(path).read()))