import os
import sys
import time
import requests

rq = requests
server = sys.argv[2]

def reader(server):
	while True:
		print("Loading messages from "+server)
		print(rq.get(server).text)
		os.system("clear")
		time.sleep(5)

def sender(server):
	username = sys.argv[1]
	while True:
		msg = input("> ")
		rq.getconf(server + "/process.php?u="+username+"&msg="+msg)
		time.sleep(1)

sender(server)