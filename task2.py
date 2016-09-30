def is_vowel(char):
    return char.lower() in ['a', 'e', 'i', 'o', 'u']

letter = input("enter any letter: ")
print(is_vowel(letter))


