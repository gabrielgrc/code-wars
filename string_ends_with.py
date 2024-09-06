#Complexity Analysis : Time O(n) | Space O(n)
def stringEndsWith(text, ending):
    if len(text) < len(ending):
        return False
    return text[-len(ending):] == ending

print(stringEndsWith("hello", "lo"))
