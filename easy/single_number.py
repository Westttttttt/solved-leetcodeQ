# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

#this solution need XOR knowledge to solve since similar no xor is 0 
def single_number(nums):
    single = 0
    for num in nums:
        single = single ^ num
    return single

nums = [0, 1, 2, 1, 2]

print(single_number(nums))