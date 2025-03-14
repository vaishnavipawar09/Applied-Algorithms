def enchantedStones(nums, k):
    nums.sort()
    length = len(nums)
    smallestscore = nums[-1] - nums[0]

    for ctn in range(length - 1):
            
        minimum_no = min(nums[0] + k, nums[ctn + 1] - k)
        maximum_no = max(nums[-1] - k, nums[ctn] + k)
        
        smallestscore = min(smallestscore, maximum_no - minimum_no)

    return smallestscore

# Test cases
print(enchantedStones([1, 3, 6], 3))  # Output: 3
print(enchantedStones([0, 10], 2))    # Output: 6




