# a program to achieve N in min number of operations
# 2 way is possible; double the number, add one to the number
# exp. from 0 to N=8, using 2 way above, how many instructions are needed?



def minNumberOfOperations(N):
  # counter is initialized
  counter=0
  
  # we can go reversely, starting from N to 0
  while N!=0:
      #increase counter for each operation
      counter=counter+1
      if N%2==0:
          N=N//2
      else:
          N=N-1
  
  return counter

print(minNumberOfOperations(7))

