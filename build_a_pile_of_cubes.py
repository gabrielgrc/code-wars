#Complexity Analysis : Time O(n) | Space O(1)
def findNb(m):
    n = 0
    totalVolume = 0
    while totalVolume < m:
        n += 1
        totalVolume += n ** 3
        if totalVolume == m:
            return n
    return -1

print(findNb(1071225))
