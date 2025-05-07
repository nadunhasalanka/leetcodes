def longestConsecutive(self, nums):
    maximum = 0
    count = 0
    sortedarray = sorted(nums)
    # print(sortedarray)

    if (len(nums) == 0):
        return 0
    elif (len(nums) == 1):
        return 1
    else:
        count = 1
        
    for i in range(0 ,len(sortedarray) - 1):
        # print("count = ",count, "max = ", maximum, "number = ", sortedarray[i])
        if ( sortedarray[i+1] == sortedarray[i] + 1 ):
            count = count + 1
        elif not ((sortedarray[i+1] == sortedarray[i])):
            if (maximum <= count):
                maximum =  count
                count = 1
                # print(maximum)
            else:
                count = 1

            # print(i, (len(sortedarray) - 2))
        if ( i == (len(sortedarray) - 2)):
                
            if (maximum < count):
                maximum =  count
                count = 1
                # print("end",maximum)

        # print("count",count, "max",maximum)
            
    return maximum

# the initial idea of the problem is this.
# first sort the array and then check if that is empty or not if empty then return 0
# if not empty then check if the length of the array is 1 then return 1
# if not then check if the next number is equal to the current number + 1
# if yes then increase the count by 1
# if it is not then check if the count is greater than the maximum
# if it is then update the maximum
# if it is not then check if the next number is equal to the current number

# there are some things that this can improve , like the time complexity of the code is O(nlogn) because of the sorting of the array.
# and there are repeating code segmanets so we can make a new function for taht.(like checking the maximum and the count)

