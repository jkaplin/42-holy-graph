#!/usr/bin/env python
import os
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
	path = ""
	try:
		path = filename[:filename.rindex('/')] + '/'
	except:
		pass
	os.system('gcc -Wall -Werror -Wextra -o ' + filename.split('.')[0] + ' ' + path + 'main.c ' + filename)
else:
	print 'Usage: compile /path/to/exname.c'
