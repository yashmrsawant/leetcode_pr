def twoSum(self, nums, target):
    
    
    sum_map = {}
    res = []
    for i in range(len(nums)):
        sum_map[nums[i]] = [i, target - nums[i]]
        f = 0
        try:
            sum_map[sum_map[nums[i]][1]]
            f = 1
            if sum_map[nums[i]][1] == nums[i]:
                f = 0
        except:
            f = 0
        
        if f == 1:
            res = [i, sum_map[sum_map[nums[i]][1]][0]]
            # print(res)
    
    if target % 2 == 0:
        a2 = []
        c = 0
        for num in nums:
            if num == target/2:
                a2.append(c)
            c = c + 1
        if len(a2) >= 2:
            res = [a2[0], a2[1]]
            
    return res

nums = [2,4,11,3]
target = 6

print(twoSum(None, nums, target)) # [0, 3]