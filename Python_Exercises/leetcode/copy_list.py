#a program to copy a list

list=[1,2,3,4]

# #easiest way to copy is assigning a list to another
# list1=list
# print(list1)





# #using slicing to copy a list
# def copyList(my_list):
# 	new_list=my_list[:]
# 	return new_list

# copied_list=copyList(list)
# print(list)
# print(copied_list)
	



# #using extend method to copy a list in a blank list
# to_be_copied=[]
# to_be_copied.extend(list)
# print(to_be_copied)





# #using shallow copy-reference- and copy()-value- func are other options
# import copy as cp

# copied_list=cp.copy(list)
# print(copied_list)


# new_list=list.copy()
# print(new_list)






# #using the enumerate func
# copied_list=[i for a,i in enumerate(list)]
# print(copied_list)





#using map func to copy a list (list variable which is defined above needs to be in a command line to execute here)
# list1=[3,5,6]
# copied_list=list(map(int,list1))
# print(copied_list)




#using slice function to copy
# copied_list=list[slice(len(list))]
# print(copied_list)





# #using list comprehension is another way
# copied_list=[i for i in list]
# print(copied_list)


