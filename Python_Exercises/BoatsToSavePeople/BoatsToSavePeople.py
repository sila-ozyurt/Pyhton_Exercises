
def numRescueBoats(self, people: List[int], limit: int) -> int:
     # Sorting the people list based on their weights.
    people.sort()
    # Initializing the variable to keep track of the number of boats used.
    boat = 0
    # Using two pointers to represent the beginning and end of the list.
    left, right = 0, len(people) - 1
        
    # Looping until the left pointer surpasses the right pointer.
    while left <= right:
         # Assuming that at least one boat will be used at each step.
        boat += 1
        # If the total weight of two people exceeds the given limit, move the right pointer to the next person.
        if people[left] + people[right] <= limit:
            left += 1
         # If the total weight of two people does not exceed the given limit, move both the left and right pointers to the next person.
         right -= 1
        
    # Returning the number of boats used.
    return boat