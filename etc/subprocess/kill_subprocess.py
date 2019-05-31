#!/usr/bin/env python
import subprocess
 

luigi_app = subprocess.Popen(run_list, cwd=scheduler_directory, env=my_env, shell=False, stdout=sys.stdout, stderr=sys.stderr)

