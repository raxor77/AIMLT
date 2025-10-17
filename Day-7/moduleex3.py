import os
import inspect

# print('current Directory',os.getcwd())

# functions=inspect.getmembers(os, inspect.isbuiltin)

# print('All Function of OS Module :')
# for n, func in functions:
#     print(n)


#create a folder inside current directory using python

# cdir=os.getcwd()
# folder_name=input('Enter Foder Name: \t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder alredy exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')


##Rename the folder
#os.rename(folder_name,'renamed folder')

dirs=os.listdir()
for dr in dirs:
    print(dr)

cdir=os.getcwd()
folder_name=input('check exist folder: \t')
folder_path=os.path.join(cdir,folder_name)

if(os.path.exists(folder_path)):
    print('Folder exist')
    new_folder=input('Enter New name: \t')
    os.rename(folder_path,new_folder)
    print(f'{new_folder} renamed at {folder_path}')
else:
    print(f'no such folder {folder_name}')