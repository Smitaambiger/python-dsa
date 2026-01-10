# Maximum Subarray Sum (Kadane's Algorithm)
# Time: O(n), Space: O(1)

def max_subarray(nums):
    max_sum = nums[0]
    curr = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        max_sum = max(max_sum, curr)

    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
