    
nums = [1, 2]
k = 2
def topKFrequent(nums, k):
    mp = {}

    for number in nums:
        if (mp.get(number, "None") != "None"):
            mp[number] = mp[number] + 1
        else:
            mp[number] = 1

    # here this line will return the sorted dictionaly by the values of  it and output will be the keys if the dictionary
    sorted_dict = (sorted(mp, key = mp.get, reverse = True))
    # print(sorted_dict)  
    slised_dict_values = []

    for i in range(k):
        slised_dict_values.append(sorted_dict[i])
    return sorted_dict

print(topKFrequent(nums, k))

# Idea is to group anagrams together with the same key value
# first sort the dictionary by the values of it and output will be the keys if the dictionary
# then slice the dictionary to get the top k frequent elements
# and return the values of the dictionary as a list of lists.
# complexity ?
#       # Time complexity: O(nlog n) , because of the sorting of the dictionary
# but without using the for loop to slice the dictionary
# we can use the slising like this:
                    # sorted_dict[:k]
                    # this will return the first k elements of the sorted dictionary
                    # and after using this the time comlexity also goes down
