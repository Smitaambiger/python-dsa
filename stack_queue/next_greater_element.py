def next_greater(nums):
    stack = []
    res = [-1]*len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)

    return res

print(next_greater([4,5,2,25]))
