import os
filepath=r'C:\AIML\Day-8\oursample' 
filename=input('Enter file name to read : ')
fullpath=os.path.join(filepath,filename) 
if(os.path.exists(fullpath)):
    #open create file and update contents
    file=open(fullpath,'r')
    content=file.read()
    print('File contents as follow :')
    print(content)
    file.close()
else:
    print('File Not Exist in folder')