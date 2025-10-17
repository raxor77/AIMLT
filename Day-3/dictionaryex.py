print('Example of dictionary')    #'keys':'values' came pair
our_dic=[
    {'id':'1', "name":'sam', "age":'35'}, 
    {"id":'2', "name":'abdul', "age":'31'}, 
    {"id":'3', "name":'yusuf', "age":'20'}, 
    {"id":'5', "name":'ramlah', "age":'42'}, 
    ]
for k in our_dic:
    print(k['id']+'->'+k['name']+'->'+k['age'])