import os

# #file_path=r'C:\AIML\Day-8\oursample\sample.txt'
# file_path='C:\\AIML\\Day-8\\oursample\\sample.txt' #<to read without r same result as above
# file=open(file_path,'w')
# content=input('enter text to write in file : ')
# file.write(content)
# file.close()

filepath=r'C:\AIML\Day-8\oursample' 
#filepath=os.getcwd() #Also can use getcwd but create n write in current folder
filename=input('Enter file name to create File : ')

fullpath=os.path.join(filepath,filename) #< create file with name in path

#open create file and writing contents
file=open(fullpath,'w')
content=input('enter text to write in file : ')
file.write(content)
file.close()
print(f'File {filename} create at {fullpath} and contents save in file')