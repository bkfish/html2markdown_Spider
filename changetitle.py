import os
import re
filePath='F:/zerokin9/blog/source/_posts/php-shenji'
count=1
for file in os.listdir(filePath):
    #title=file[0:-3]
    print(file)
    with open(os.path.join(filePath,file), "r+",encoding='utf-8') as f:
        #old = f.read()
        f.readline()
        old_title=f.readline()[7:-1]
        title=old_title.replace('[','').replace(']','').replace('<','').replace('>','').replace('!','').replace('_','').replace(' ','').replace('-','')
        #f.seek(0)
        print(title)
        f.seek(0)
        f.write("---\ntitle: "+title+"\n---\n\n")
    #os.rename(os.path.join(filePath,file),os.path.join(filePath,title+".md"))   
    count+=1
print(count)
