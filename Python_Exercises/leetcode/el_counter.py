# a program to calculate the number of x in a list
def elementCounter(list,x):
    #start the counter from 0
    c=0
    for i in list:
        #when the value is equal to x, add one to the counter
        if i==x:
            c+=1
    #return the value of counter
    return c


list=[5,6,7,8,4,4,4]
print(elementCounter(list,4))