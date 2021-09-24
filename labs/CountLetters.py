#Take a word as input and count how many letters, how many vowels and how many consonants

Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Vowels = ['A', 'E', 'I', 'O', 'U']
consonates = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'y']

def isWord(s):
    if s.strip().isdigit():
        return False
    else:
        return True

print("please type in a word and I will output how many letters, vowels, and consonates are in the word")
word = input()
print(word)

while isWord(word):
    print("Please type in a word and not a integer")
    word = input()
    if not isWord(word):
        break
print(word)


