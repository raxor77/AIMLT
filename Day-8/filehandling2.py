import os
filepath=r'C:\AIML\Day-8\oursample' 
filename=input('Enter file name to update : ')
fullpath=os.path.join(filepath,filename) 
if(os.path.exists(fullpath)):
    #open create file and update contents
    file=open(fullpath,'a')
    content=input('enter text to write in file : ')
    file.write(content)
    file.close()
    print(f'File {filename} updated')
else:
    print('File Not Exist in folder')