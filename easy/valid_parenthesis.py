# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


def is_valid(s):
    ans = []

    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            ans.append(ch)    
        else:
            if ch == ")" :
                ans.pop() if ans and ans[-1] == "(" else ans.append(ch)
            elif ch == "]":
                ans.pop() if ans and ans[-1] == "[" else ans.append(ch)
            else :
                ans.pop() if ans and ans[-1] == "{" else ans.append(ch)
    
    return len(ans) == 0

s = "()[]{}"
print(is_valid(s))

#time complexity = O(n)
#space complexity = O(n)