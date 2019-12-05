#!/usr/bin/python3
import os

def helper_get_path(f):
    return os.path.dirname(os.path.realpath(f))

PROJ_PATH = helper_get_path(__file__) + '/'
print(PROJ_PATH)
PAGE_TITLE = '5CTF'
