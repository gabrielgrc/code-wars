#Complexity Analysis : Time O(m * n) | Space O(n)
def stripComments(string, markers):
    lines = string.split('\n')
    resultLines = []

    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
        resultLines.append(line.rstrip())
        
    return '\n'.join(resultLines)

print(stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
