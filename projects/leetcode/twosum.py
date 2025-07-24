target = 5
nums = [1,4,71,614,6,12,8]
count_2 =  0
count = 0
while count_2 <= len(nums):
    while count <= len(nums)-1:
        count += 1
        if count <= len(nums)-1 and count_2 <= len(nums)-1 and ((nums[count] + nums[count_2]) == target) and count_2 != count:
            print([count_2, count])
            break
    count_2 += 1
    count = 0