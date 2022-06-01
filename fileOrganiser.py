import shutil
import os
import time
path=input("Enter the name of the directory to e sorted :")
days=time.time()
listOfFiles=os.listdir(path)
for file in listOfFiles :
    name,ext=os.path.splitext(file)
    ext=ext[1:]

    if ext=='' :
        continue
    if os.path.exists(path+'/'+ext) :
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file) 
    else :
        os.makedirs(path + '/' + ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file) 