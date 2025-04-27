# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x = 121    

def is_palindrome(x):
    if x < 0 or ( x % 10 == 0 and x != 0) :
        return False

    temp_x = x
    temp = 0
    while x > 0:
        digit = x % 10
        temp = 10 * temp + digit
        x = x // 10
    
    print(temp)
    print(temp_x)
    return temp == temp_x

print(is_palindrome(x))

##time complexity -> O(log n)
# space complexity -> O(1)