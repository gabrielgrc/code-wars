#Complexity Analysis : Time O(n*log(n)) | Space O(1)
def findUniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]

#Complexity Analysis : Time O(n) | Space O(n)
# def findUniq(arr):
#     charCount = {}

#     for char in arr:
#         if char in charCount:
#             charCount[char] += 1
#         else:
#             charCount[char] = 1
    
#     return next((key for key, value in charCount.items() if value == 1), None)

print(findUniq([ 1, 1, 1, 2, 1, 1 ]))
