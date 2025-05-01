# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


#this approach use O(n) space complexity so, m gonna optimise a little bit to get O(1) space complexity
# def majority_element(nums):
#     hashmap = {}
#     for num in nums:
#         #if the num is already in the hashmap just add 1 
#         if num in hashmap :
#             hashmap[num] += 1
#         #if not just initialized with the value 1
#         else:
#             hashmap[num] = 1
        
#         if hashmap[num] > len(nums) / 2 :
#             return num


#now this approach takes only O(1) space complexity ============================
## Suprizing this algorithm is called Boyer-Moore Algorithm , hahha i naver heard of it, But to think that, i just make Boyer-Moore Algo, with my own intuition ,What a nice achievement


def majority_element(nums):
    majority = None
    freq = 0

    for num in nums :
        if freq <= 0 :
            majority = num
            freq = 1
        elif majority != num:
            freq -= 1
        else :
            freq += 1

    return majority


nums = [3, 2, 3]
print(majority_element(nums))