# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#====================================Points to be remember in order to find the ans========================
## Each input would have exactly one solution 
## We cant use the same element twice
## i can return the ans in any order
#============================================================================================

#Approach->
# 1. Loop over the nums and in every iteration i have to substract the curr num and the target and have to store it in a variable called no_to_find
# 2. I Check if the no_to_find variable is already in the hash map, if so we found the ans , else we add the curr num to the hashmap with its index as a value


nums = [2, 11, 7, 15] ## ans = [0, 2] since 2 and 7 is 9
target = 9

def two_sum(nums, target):  
    hashmap = {}
    ans = []
    for i in range(len(nums)):
        no_to_find = target - nums[i]

        if(no_to_find in hashmap): 
            ans.append(hashmap[no_to_find])
            ans.append(i)
            return ans
        else : 
            hashmap[nums[i]] = i 

    return ans

print(two_sum(nums, target))

## time complexity => o(n)
## space complxity => o(n)
