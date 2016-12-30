#!/usr/bin/env python

import subprocess
import os

def execute(command):
	try:
		istatus = subprocess.check_call(command,shell=True)
	except subprocess.CalledProcessError:
		istatus = 1
	return istatus

def append_to_log(jobstatus,pseudopid,command_str,now):
	home = subprocess.check_output('echo $HOME',shell=True).replace('\n','')
	if not os.path.isdir(home + '/.followR/'):
		os.system('mkdir ' + home + '/.followR/')
	f = open(home + '/.followR/follow.log','a')
	f.write(jobstatus + ' ' + pseudopid + ' ' + command_str + ' ' + \
                now.strftime('%Y-%m-%d@%H:%M') + '\n')
	f.close()
	return None

def command_as_string(command):
	out=''
	if len(command) == 1:
		out = command[0]
	else:
		for item in command:
			out = out + ' ' + item
	return out

