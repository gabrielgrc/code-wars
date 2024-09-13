#Complexity Analysis : Time O(n) | Space O(1)
def countBits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

print(countBits(1234))

#Complexity Analysis : Time O(log(n)) | Space O(log(n))
# def countBits(n):
#     binaryRepresentation = bin(n)[2:]

#     count = 0
#     for num in binaryRepresentation:
#         if num == '1':
#             count += 1
#     return count
# print(countBits(1234))
