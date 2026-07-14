def twoSum(nums, target):
    left,right = 0 , len(nums)-1
    while left < right :
        if nums[left] + nums[right] < target:
            left +=1
        elif nums[left]+nums[right] > target:
            right -=1
        else:
            return [left,right]

    return []


result = twoSum([4, 5, 10, 20], 9)

# 4. Print the result
print(result)







