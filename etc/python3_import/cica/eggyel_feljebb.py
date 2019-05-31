#!/usr/bin/env python

import os
import sys

base_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(base_path, ".."))

from kutya.f import msg

if __name__ == '__main__':
	msg()