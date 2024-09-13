#Complexity Analysis : Time O(n) | Space O(n)
def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < len(signature):
        return signature[:n]
    
    result = signature[:n]
    
    while len(result) < n:
        nextValue = result[-1] + result[-2] + result[-3]
        result.append(nextValue)
    
    return result

print(tribonacci([1, 1, 1], 10))

#Complexity Analysis : Time O(n) | Space O(n)
# def tribonacci(signature, n):
#     if n == 0:
#         return []
#     elif n < len(signature):
#         return signature[:n]
    
#     while len(signature) < n:
#         signature.append(signature[-1] + signature[-2] + signature[-3])
    
#     return signature

# print(tribonacci([1, 1, 1], 10))
