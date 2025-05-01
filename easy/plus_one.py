# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

nums = [9,9,9]

def plus_one(nums):
    if nums[len(nums) - 1] == 9:
        nums.pop()
        # nums.append(1)
        nums.append(0)

        if nums[len(nums) - 2] == 9:
            nums.pop()
            nums.append(0)
    else : 
        nums[len(nums) - 1] += 1

    return nums

print(plus_one(nums))