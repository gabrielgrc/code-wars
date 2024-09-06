#Complexity Analysis : Time O(n) | Space O(n)
def toCamelCase(text):
    if not text:
        return text

    words = text.replace('-', ' ').replace('_', ' ').split()

    camelCaseText = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camelCaseText

print(toCamelCase("the-stealth-warrior"))
