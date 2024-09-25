#Complexity Analysis : Time O(n) | Space O(n)
def pigIt(text):
    words = text.split()
    transformedWords = []

    for word in words:
        if word.isalpha():
            newWord = word[1:] + word[0] + "ay"
        else:
            newWord = word
        transformedWords.append(newWord)
        
    return ' '.join(transformedWords)

print(pigIt('Pig latin is cool'))
#print(pigIt('Hello world !'))
