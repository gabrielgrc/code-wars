#Complexity Analysis : Time O(n) | Space O(n)
def countCharacters(s):
    charCount = {}
    
    for char in s:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    
    return charCount


print(countCharacters('aba'))
