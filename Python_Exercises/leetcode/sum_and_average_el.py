# a program to find a sum and average elements of a list with a function

# function which computes the sum of the elements in the given list
def findSum(lst):
    #sum value needs to be started from 0
    sum = 0
    # each element is added orderly
    for i in lst:
        sum += i
    return sum

# function to calculate average value of numbers in the list
def findAverage(lst):
    #first wee need to get the length of the list in a variable
    length = len(lst)
    return findSum(lst) / length


lst = [1, 2, 3, 4, 5]
print("List: [1, 2, 3, 4, 5]")

try:
    #which operation the user demands to perform is asked
    outcome = int(input("Which operation do you want to pearform?\n1-Find sum of the list\n2-Find average of the list\n"))

    # according to the answers, needed operations are done
    if outcome == 1:
        output = findSum(lst)
        print("Sum of the list:", output)
    elif outcome == 2:
        output = findAverage(lst)
        print("Average of the list:", output)
    else:
        print("Please enter a valid option (1 or 2)!")

#in case, the user enters an invalid value
except ValueError:
    print("Invalid input! Please enter a number.")
#in case, the program gives an error for some unknown reasons
except Exception as e:
    print("An error occurred:", e)