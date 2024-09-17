#Complexity Analysis : Time O(n) | Space O(n)
def splitStrings(s):
    pairs = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        if len(pair) == 1:
            pair += '_'
        pairs.append(pair)
    return pairs

print(splitStrings('abcdef'))
#print(splitStrings('abc'))
