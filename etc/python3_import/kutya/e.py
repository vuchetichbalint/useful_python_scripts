import importlib.util

def mukodike():
	spec = importlib.util.spec_from_file_location('cica.d', '/home/balint/workspace/hasznos_scriptek/python3_import/cica/d.py' )
	foo = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(foo)
	foo.bar()		


	print('tenyleg!')

mukodike()

