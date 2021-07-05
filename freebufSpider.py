# -*- coding: UTF-8 -*-
import os
import sys
import getopt
import requests
import random
import re
import time
import json
import html2text
from bs4 import BeautifulSoup
import argparse
useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
headers = {
    'User-Agent': random.choice(useragents)
}

def freebuf_spider(url):
    ## 获取网页主体
    print(url)
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'html.parser')
    pwd = os.getcwd() # 获取当前的文件路径
    dirpath = pwd + '/freebuf_ctf/'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath) 
    try:
	    title = soup.find_all('title')[0].get_text()
	    article = str(soup.find_all("div",id="tinymce-editor")[0])
	    #print(article)
	    title=title.replace('?','-').replace('*','-').replace('|','-').replace('=','-').replace(':','-').replace('\'','-').replace('"','-').replace('：','-').replace('】','-').replace('【','-').replace('/','-').replace('\\','-').replace('[','').replace(']','').replace('<','').replace('>','').replace('!','').replace('_','').replace(' ','').replace('-','')[0:30]
	    write2md(dirpath,title,article)
    #print(html)
    except Exception as e:
    	raise e
    	return


def write2md(dirpath,title,article):
    ## 创建转换器
    h2md = html2text.HTML2Text()
    h2md.ignore_links = False
    ## 转换文档
    article = h2md.handle(article)
    ## 写入文件
    if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
        os.makedirs(dirpath)
    # 创建md文件
    with open(dirpath+title+'.md','w',encoding="utf8") as f:
        lines = article.splitlines()
        for line in lines:
            if line.endswith('-'):
                f.write(line)
            else:
                f.write(line+"\n")
    print(title+"下载完成....")
for i in range(1,100):
    out_json=requests.get('https://search.freebuf.com/search/find/?content=ctf&page='+str(i)).text
    out_json=json.loads(out_json)
    for i in out_json['data']['list']:
        try:
            url=i['url']
            freebuf_spider(url)
        except:
            pass

print("爬取博文完毕\n------------------\n")

pro_dir="./freebuf_ctf/"
if not os.path.exists(pro_dir):# 判断目录是否存在，不存在则创建新的目录
    os.makedirs(pro_dir)
dirs=os.listdir(pro_dir)
def model_picture_download(model_picture_url, file_dir,text,new_pic):
    headers = {
        'User-Agent': random.choice(useragents)
    }
    model_picture_downloaded = False
    err_status = 0
    while model_picture_downloaded is False and err_status < 10:
        try:
            html_model_picture = requests.get(
                model_picture_url,headers=headers, timeout=1)
            with open(file_dir, 'wb') as file:
                file.write(html_model_picture.content)
                model_picture_downloaded = True
                text=text.replace(pic_url,"./img/"+new_pic)
                print('下载成功！图片 = ')
                return text
        except Exception as e:
            err_status += 1
            random_int = 4
            time.sleep(random_int)
            print(e)
            print('出现异常！睡眠 ' + str(random_int) + ' 秒')
            return text
        continue
    return text



print("正在更换图床\n")
img_path="./freebuf_ctf/img"
try:
    os.makedirs(img_path)
except:
    pass
for file in dirs:
    if file!="img":
        f=open(pro_dir+file,"r+",encoding='utf-8')
        text=f.read()
        f.close()
        print(file)
        #print(text)
        pic_list=re.findall(r"!\[.+?\]\(.+?\)", text) #找到了所有文件
        for pic in pic_list:
            pic_url=pic[4:].split('](')[1].replace(")","")
            print(pic_url)
            new_pic=str(hash(pic_url))+'.png'
            new_pic=new_pic.replace("-","")
            try:
                text=model_picture_download(pic_url, pro_dir+'img/'+new_pic,text,new_pic)
                print(pic_url)
                print(new_pic)
            except Exception as e:
                print(e)
            continue
            
        f=open(pro_dir+file,"w+",encoding='utf-8')
        f.write(text)
        f.close()