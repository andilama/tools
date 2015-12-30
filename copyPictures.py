# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:22:04 2013

@author: Andi
"""

import argparse
import os
import shutil

def samsung():
    print "Samsung"
    
def sony():
    print "Sony"
    
def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("option", help="Choose to process pictures \
    from Sony or Samsung")
    args = parser.parse_args()
    if args.option == "Sony":
        sony()
    elif args.option == "Samsung":
        samsung()
        

start()
    


