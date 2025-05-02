mp = {}
gpangram = ["ate","eat"]
def groupAnagrams(self, gpangram):
    for word in gpangram:
        sortedWord = (''.join(sorted(word)))

        if (mp.get(sortedWord, "None") != "None"):
            mp[sortedWord].append(word)
        else:
            mp[sortedWord] = [word]
    
    return mp.values()

print(groupAnagrams(mp, gpangram))


# Idea is to group anagrams together with the same key value
# and then return the values of the dictionary as a list of lists.
# complexity ?
      # Time complexity: O(n * k log k)
      # k log k is the time complexity of sorting a string of length k.
      # n is the number of strings in the input list.