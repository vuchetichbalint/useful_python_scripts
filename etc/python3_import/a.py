import importlib.util
import sys

dir_path = '/Users/balint/workspace/hasznos_scriptek/python3_import/kutya'
file_path = '/Users/balint/workspace/hasznos_scriptek/python3_import/kutya/c.py'


sys.path.append(dir_path)
import c as kty

"""
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
"""




#from b import bar

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)

def mukodike():
	kty.bar()
	print('tenyleg!')

mukodike()

