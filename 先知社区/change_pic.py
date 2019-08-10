import os
import re
from urllib.request import urlretrieve
from urllib import error
import requests
import time
import random
pro_dir="./test/"
dirs=os.listdir(pro_dir)
useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
# 下载模特图片
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

for file in dirs:
	if file!="img":
		f=open(pro_dir+file,"r+",encoding='utf-8')
		text=f.read()
		f.close()
		print(file)
		#print(text)
		pic_list=re.findall(r"!\[\]\(.+?\)", text) #找到了所有文件
		for pic in pic_list:
			pic_url=pic[4:].split('\)')[0].replace(")","")
			#print(pic_url)
			new_pic=str(hash(pic_url))+'.png'
			new_pic=new_pic.replace("-","")
			try:
				text=model_picture_download(pic_url, pro_dir+'img/'+new_pic,text,new_pic)
				print(pic_url)
				print(new_pic)
				
			except error.URLError as e:
				raise e
			continue
			
		f=open(pro_dir+file,"w+",encoding='utf-8')
		f.write(text)
		f.close()