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

useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]

def jianshu(url):
    if url=='':
        #print("爆炸boom")
        return
    ## 浏览器头部
    headers = {
        'Host': 'www.jianshu.com',
        'Referer': 'https://www.jianshu.com/',
        'User-Agent': random.choice(useragents)
    }
    ## 获取网页主体
    html = requests.get(url,headers=headers).text

    ## bs4
    soup = BeautifulSoup(html,"lxml")
    title = soup.find_all("title")[0].get_text()
    article = str(soup.find_all("div",class_="show-content")[0])

    ## 替图片的src加上https://方便访问
    article = re.sub('(src=")|(data-original-src=")','src="https:',article)

    ## 写入文件
    pwd = os.getcwd() # 获取当前的文件路径
    dirpath = pwd + '/jianshu/'
    write2md(dirpath,title,article)

def doelse(url):
    headers = {
        'User-Agent': random.choice(useragents)
    }
    res = requests.get(url=url ,headers=headers) # 获取整个html页面

    h = html2text.HTML2Text()
    h.ignore_links = False
    soup = BeautifulSoup(res.text,'lxml')
    title = soup.title.text # 获取标题
    html = str(soup.body)
    article = h.handle(html)

    pwd = os.getcwd() # 获取当前文件的路径
    dirpath = pwd + '/Else/'
    if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
        os.makedirs(dirpath)
    ## 写入文件
    write2md(dirpath,title,article)
    

"""
传入文件路径，title，article
"""
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
    with open('./jianshu1/'+title[0:37]+'.md','w',encoding="utf8") as f:
        lines = article.splitlines()
        for line in lines:
            if line.endswith('-'):
                f.write(line)
            else:
                f.write(line+"\n")
    print(title+"下载完成....")


def get_page_url(page_id):
    url="https://www.jianshu.com/search/do?q=PostgreSQL 源码解读（"+str(page_id)+"）&type=note&page=1&order_by=default"
    print(url)
    ## 浏览器头部
    headers = {
        'Host': 'www.jianshu.com',
        'Referer': 'https://www.jianshu.com/',
        'User-Agent': random.choice(useragents)
    }
    s=requests.post(url,headers=headers)
    text=s.content.decode('utf-8')
    tmp = json.loads(text)
    obj_url=''
    try:
        obj_num=tmp['entries'][0]['slug']
        obj_url='https://www.jianshu.com/p/'+obj_num
    except KeyError as e:
        print('键错误')
    except IndexError as e:
        print('索引错误')
    except TypeError as e:
        print('类型错误')
    except ValueError as e:
        print('值的类型错误')
    except Exception as e:
        print('错误')
    return obj_url

def main(argv):
    i=1
    while (i<116):
        page_url=get_page_url(i)
        print("第"+str(i)+"篇文章的page_url： "+ page_url)
        print(page_url)
        if page_url=='':
            i=i-1
        print("i: "+str(i))
        time.sleep(2)
        jianshu(page_url)
        time.sleep(1)
        i=i+1
    
    

if __name__ == "__main__":
    main(sys.argv[1:])