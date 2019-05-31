#!/usr/bin/env python
import os 

def foo():
	print('az elet szep')
	dir_path = os.path.dirname(os.path.realpath(__file__))
	print(dir_path)

def bar():
	foo()