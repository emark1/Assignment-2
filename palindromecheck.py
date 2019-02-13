#Palindrome Checker

word = input("Please enter a word: ")
word = word.lower()
wordreversed = ""
characterlength = len(word)
while characterlength > 0:
    wordreversed += word[characterlength-1]
    characterlength = characterlength -1

if wordreversed == word:
    print("This is a palindrome")
else:
    print("Not a palindrome.")