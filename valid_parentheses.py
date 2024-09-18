#Complexity Analysis : Time O(n) | Space O(n)
def isValidParentheses(paren_str):
    stack = []

    for char in paren_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

print(isValidParentheses("()"))              # True
# print(isValidParentheses(")(()))"))          # False
# print(isValidParentheses("("))               # False
# print(isValidParentheses("(())((()())())"))  # True
