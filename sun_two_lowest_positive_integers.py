#Complexity Analysis : Time O(n) | Space O(1)
def sumTwoSmallestNumbers(numbers):
    min1, min2 = float('inf'), float('inf')

    for num in numbers:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return min1 + min2

#Complexity Analysis : Time O(n*log(n)) | Space O(n)
# def sumTwoSmallestNumbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]

print(sumTwoSmallestNumbers([19, 5, 42, 2, 77]))
