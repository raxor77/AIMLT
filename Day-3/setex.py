#print('Sets in Python')

# set_1={'laptop', 'mobile', 'airpod', 'ipad', 'iphone', 'laptop', 'android phone', 'mobile'}
# print('numbers of items in set :', len(set_1))
# for item in set_1:
#     print(item, end=" ")  # set will not show repeated items

#clear() : remove all items in sets
# set_1={'laptop', 'mobile', 'airpod', 'ipad', 'iphone', 'laptop', 'android phone', 'mobile'}
# set_1.clear()
# print('After clear numbers of items in set_1 are:', len(set_1))
# for item in set_1:
#     print(item, end=" ") 

#set.remove(item): Update the set and remove item from set 
# set_1={'laptop', 'mobile', 'airpod', 'ipad', 'iphone', 'android phone'}
# print('numbers of items in set :', len(set_1))
# for item in set_1:
#     print(item, end=" ")
# set_1.remove('mobile')
# print('\nset after removing one item from set:', len(set_1))
# for item in set_1:
#     print(item, end=" ")


#union, intersection, difference
# set_1={100,200,500,700,900,150,450}
# set_2={1000,100,250,555,700}
# set_3={100,100,200,5550,7000}
# #union
# #s2.union(s2): Return anew set with new items from both set s1 s2 without duplication
# print(f'set_1 contain {len(set_1)}items')
# print(set_1)
# print(f'set_2 contain {len(set_2)}items')
# print(set_2)
# print(f'set_2 contain {len(set_3)}items')
# print(set_3)
# unionset=set_1.union(set_2,set_3)
# print(f'union set of set_1 and set_2 and set_3, contain {len(unionset)} following items')
# print(unionset)

#intersection
# set_1={100,200,500,700,900,150,450}
# set_2={1000,100,250,555,700}
# # s1.intersection(s2): Return a new set which only contain both  from both set s1 s2
# print(f'set_1 contain {len(set_1)}items')
# print(set_1)
# print(f'set_2 contain {len(set_2)}items')
# print(set_2)
# intrctnset=set_1.intersection(set_2)
# print(f'intersection set of set_1 and set_2 contain {len(intrctnset)} following items')
# print(intrctnset)

#difference
set_1={100,200,500,700,900,150,450}
set_2={1000,100,250,500,700}
# s1.difference(s2): Return a new set which only contain those are in s1 not in s2
print(f'set_1 contain {len(set_1)}items')
print(set_1)
print(f'set_2 contain {len(set_2)}items')
print(set_2)
diffset=set_1.difference(set_2)
print(f'difference of set_1 compare to, set_2, contain {len(diffset)} following items')
print(diffset) #result display which only diff from s1.