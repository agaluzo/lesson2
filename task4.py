import random


def read_words(filename='20k.txt'):
    """ Read file of most popular english words"""
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if
             len(word) > 5]
    return words


def choose_random_word(words):
    """ Choose random word from list """
    return random.choice(words)


def update_available_letters(letters, char):
    updated_available_letters = letters.replace(char, "")
    return updated_available_letters


def update_guessed_word(word, guess_word, char):
    updated_guessed_word = guess_word
    for i, letter in enumerate(word):
        if letter == char:
            updated_guessed_word = updated_guessed_word[0:i] + char + updated_guessed_word[i + 1:]
    return updated_guessed_word


def main():
    hidden_word = choose_random_word(read_words())
    guessed_word = '_' * len(hidden_word)
    guesses = 8
    available_letters = 'abcdefghijklmnopqrstuvwxyz'

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.' % len(hidden_word))
    print(guessed_word)

    while guesses != 0 and hidden_word != guessed_word:
        print('You have %d guesses left' % guesses)
        print('available letters: %s' % available_letters)
        letter = str(input('Please guess a letter: ').lower())
        if letter in hidden_word:
            guessed_word = update_guessed_word(hidden_word, guessed_word, letter)
            available_letters = update_available_letters(available_letters, letter)
            print("Good guess: " + guessed_word)
        elif letter not in available_letters:
            print("Oops! Probably you have entered this letter already. Please try again: " + guessed_word)
        else:
            print("Oops! That letter is not in my word: " + guessed_word)
            guesses -= 1
            available_letters = update_available_letters(available_letters, letter)

    if guesses == 0:
        print("Sorry, but you lost.")
        print("The word I am thinking is '" + hidden_word + "'")
    else:
        print("You won.")

if __name__ == "__main__":
    main()
