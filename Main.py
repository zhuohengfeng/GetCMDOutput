#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from subprocess import *
proc = Popen('start.bat', stdin=PIPE, stdout=PIPE, shell=True)
sys.setdefaultencoding('utf-8')
while True:
        line = proc.stdout.readline()
        if not line:
            break
        print(line)