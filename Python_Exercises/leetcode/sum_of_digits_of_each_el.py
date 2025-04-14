# a program which adds up each digits in each element
# let's suppose list=[21, 45, 77] is given, output is out=[3,9,14]



#first way is nested for loops

def addDigits(lst):

    new_list=[]
    for i in lst:
        # we have to start this variable here because as it moves to the next element, it will zero itself 
        sum_of_digits=0
        # make i values string to divide numbers, such as 12 -> 1  2
        for j in str(i):
            #we need to set j value as int to perform summation properly.
            sum_of_digits+=int(j)
        # place the values on list one by one
        new_list.append(sum_of_digits)

    return new_list


# list=[21,34,56]
# print(addDigits(list))



# a second way to perform the same operation
#bu program bitmeid