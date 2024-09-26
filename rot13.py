#Complexity Analysis : Time O(n) | Space O(n)
def rot13(message):
    result = []

    for char in message:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))

        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))

        else:
            result.append(char)

    return ''.join(result)

print(rot13("EBG13 rknzcyr."))
