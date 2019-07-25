import os
import re
import requests
f=open("CTF-Writeup.txt","w+",encoding="utf-8")
for j in range(1,100):
	r_url="https://so.csdn.net/so/search/s.do?q=CTF+Writeup&t=blog&o=&s=&l=&p="+str(j)
	print("page_url:"+r_url)
	rep = requests.get(r_url)
	url_list = re.findall(r".+?\">&nbsp;-&nbsp;CSDN博客</a>", rep.content.decode('utf-8'))
	for i in url_list:
			#print(i)
			f.write(i[41:].split('"')[0]+"\n")
			print(i[41:].split('"')[0])
f.close()
#print(url_list)