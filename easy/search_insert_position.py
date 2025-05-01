# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_insert_position(nums, target):
    s, e = 0, len(nums)-1

    while s <= e:
        m = s + (e - s) // 2 #this solve left to right, we can say s+e / 2 but its not optimised...
        if nums[m] == target:
            return m
        
        if nums[m] < target:
            s = m+1
        else:
            e = m-1
    #if the target is not found we will return out s, since s will points to the index where our target should be 
    return s

nums = [1, 3, 5, 6] 
target = 4

print(search_insert_position(nums, target))
        



