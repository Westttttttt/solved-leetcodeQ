#this is how we can solve fibo in dynamic programing using memoization 
z
def fibo(n, memo={}):
    if n in memo :
        return memo[n]
    
    if n <= 2 :
        return 1
    
    memo[n] =  fibo(n - 1) + fibo(n - 2)
    return memo[n]

print(fibo(50))

#time complexity -> O(n)
#space complexity -> O(n)

#thats the power of dynamic programing we brought down to O(n) from O(2^n) whic is exponentioal