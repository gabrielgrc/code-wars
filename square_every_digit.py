#Complexity Analysis : Time O(n) | Space O(n)
def squareDigits(num):
    total = []

    for digit in str(num):
        total.append(int(digit) ** 2)
    
    return int(''.join(map(str, total)))
  
print(squareDigits(9119))
