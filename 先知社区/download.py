import os
import sys
import getopt
import requests
import random
import re
import html2text
from bs4 import BeautifulSoup
useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
    
def csdn(url):
    headers = {
        
        'User-Agent': random.choice(useragents)
    }
    ## 获取网页主体
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    pwd = os.getcwd() # 获取当前的文件路径
    dirpath = pwd + '/xianzhi/'
    title = soup.find_all('title')[0].get_text()
    article = str(soup.find_all("div",class_="topic-content markdown-body")[0])
    #print(article)
    title=title.replace('*','-').replace('|','-').replace('=','-').replace(':','-').replace('\'','-').replace('"','-').replace('：','-').replace('】','-').replace('【','-').replace('/','-').replace('\\','-').replace('[','').replace(']','').replace('<','').replace('>','').replace('!','').replace('_','').replace(' ','').replace('-','')[0:30]
    write2md(dirpath,title,article)
    #print(html)

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

#csdn("https://xz.aliyun.com/t/5745")
file = open("url_list.txt") 
for line in file.readlines():
    line=line.strip('\n')
    try:
        print(line)
        csdn(line)
    except Exception as e:
        raise e
file.close()