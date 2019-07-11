import os
import re
filePath='C:/Users/38138/Desktop/csdnphp-文件包含'
count=1
for file in os.listdir(filePath):
    title=file[0:-3].replace('*','').replace('、','').replace('[','').replace(']','').replace('<','').replace('>','').replace('#','').replace('!','').replace('_','').replace(' ','').replace('-','')
    with open(os.path.join(filePath,file), "r+",encoding='utf-8') as f:
        old = f.read()
        f.seek(0)
        f.write("---\ntitle: "+title+"\n---\n")
        f.write(old)
    count+=1
#os.rename(os.path.join(filePath,file),os.path.join(filePath,title+".md"))  
print(count)
