#Complexity Analysis : Time O(d*log(d)) | Space O(d)
def narcissistic(value):
    numDigits = len(str(value))
    total = 0

    for digit in str(value):
        total += int(digit) ** numDigits

    return total == value

print(narcissistic(153))
