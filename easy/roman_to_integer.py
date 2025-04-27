# Input: s = "III"
# Output: 3

#input: s = "IV"
#output: 4

##things to keep in mind
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def roman_to_integer(s):
    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    ans = 0
    prev_char = ""

    for ch in s:
        if ch == "I" :
            ans += I
        elif ch == "V":
            if(prev_char == "I") :
                ans += V - I - I
            else:
                ans += V
        elif ch == "X":
            if(prev_char == "I") :
                ans += X - I - I
            else :
                ans += X
        elif ch == "L":
            if(prev_char == "X"):
                ans += L - X - X
            else:
                ans += L
        elif ch == "C":
            if(prev_char == "X"):
                ans += C - X - X
            else:
                ans += C
        elif ch == "D":
            if(prev_char == "C"):
                ans += D - C - C
            else:
                ans += D
        elif ch == "M":
            if(prev_char == "C"):
                ans += M - C - C
            else:
                ans += M
        else:
            return ans

        prev_char = ch
    
    return ans

print(roman_to_integer("MCMXCIV"))

#time complexity = O(n)
#spance complexity = O(1)


#==================================Otmised===========================================
# def romanToInt(s: str) -> int:
#     values = {
#         'I': 1, 'V': 5, 'X': 10,
#         'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }
    
#     total = 0
#     prev = 0

#     for ch in reversed(s):
#         curr = values[ch]
#         if curr < prev:
#             total -= curr
#         else:
#             total += curr
#         prev = curr

#     return total
