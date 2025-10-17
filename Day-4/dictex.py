# employee={'id':1,
#           'name':'sayuti',
#           'salary':5000.60}

# print('employee details as follow : ')
# for key,value in employee.items():
#     print(key, ">", value)

# #Adding key into dictonary
# employee["city"]="muscat"
# print('\n dictonary after adding city\n')

# for key,value in employee.items():
#     print(key, '>', value)

# #Delete key in Dictonary
# del employee["salary"]
# print('\nEmployee details after delete salary')
# for key,value in employee.items():
#     print (key, '>', value)

#print all keys
employee={'id':1,
          'name':'sayuti',
          'salary':5000.60}

print('All keys from employee')
for k in employee.keys():
    print(k, end=('\t'))

print('\nAll values from employee')
for v in employee.values():
    print(v, end=('\t'))

print('keys : values')
for k,v in employee.items():
    print(k,":", v)

print('\n Dictonnary as follow :')
print(employee)