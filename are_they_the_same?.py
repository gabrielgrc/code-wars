#Complexity Analysis : Time O(n) | Space O(n)
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    freq1 = {}
    for num in array1:
        square = num ** 2
        if square in freq1:
            freq1[square] += 1
        else:
            freq1[square] = 1

    freq2 = {}
    for num in array2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1

    return freq1 == freq2

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))

#Complexity Analysis : Time O(n*log(n)) | Space O(n)
# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     if len(array1) != len(array2):
#         return False
#     squaredArray = [num ** 2 for num in array1]
#     return sorted(squaredArray) == sorted(array2)

# print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
