def longestCommonPrefix(strs):
    l3 = []
    l2 = []
    l4 = []
    for i3 in range(len(strs)):
        l4.append(len(list(strs[i3])))
    for i2 in range(min(l4)):
        for i in range(len(strs)):
            l2.append(strs [i][i2])
            if len(l2) == len(strs) and len(list(set(l2))) == 1:
                l3.append(strs [i][i2])
                l2 = []
    return "".join(l3)
print(longestCommonPrefix(["flower","flow","flight"]))
