nums = [2,7,11,15]
target = 9
c = 0
c2 = len(nums)-1
while c < len(nums)-1:
    while c2 > c:
        if nums[c]+nums[c2] == target:
            print([c,c2])
        c2 -= 1
    c += 1
    c2 = len(nums)-1