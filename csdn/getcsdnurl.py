import os
import sys
import getopt
import requests
import random
import re
import json
import time
import html2text
from bs4 import BeautifulSoup

f=open("CTF-php.txt","w+",encoding="utf-8")
for s in range(1,20):
	filename=str(s)+'.html'
	x=open(filename,"r+",encoding="utf-8")
	text=x.read()
	url_list = re.findall(r".+?\">&nbsp;-&nbsp;CSDN博客</a>", text)
	x.close()
	#print(url_list)

	for i in url_list:
		#print(i)
		f.write(i[41:].split('"')[0]+"\n")
		print(i[41:].split('"')[0])
