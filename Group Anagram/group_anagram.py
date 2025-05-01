mp = {}
gpangram = ["ate","eat"]
for word in gpangram:
    newword = (''.join(sorted(word)))

    if (mp.get(newword, "None") != "None"):
        mp[newword].append(word)
        print("hellp")
    else:
        mp[newword] = [word]
        
print(mp)
