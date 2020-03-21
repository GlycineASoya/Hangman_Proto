from typing import Dict, Any


def isletter(possible_letter: str) -> bool:
    #check the letter if it is not a null and/or a string
    if len(possible_letter) != 1:
        return False #put later an exception
    ch = ord(possible_letter)
    if (65 <= ch <= 90)\
            or (97 <= ch <= 122) \
            or ((472 <= ch <= 537) and (97 <= ch <= 122)):
        return True #put later an exception


def ispart(possible_letter: str) -> bool:
    if possible_letter in guessed_Word:
        return True
    return False


print("This is the word game called HangMan")

guessed_Word = input('To quit the program pres Esc and type \'quit\'\n\r'
                     'Please, enter the word to guess: ')

guessed_Word_Set = set(guessed_Word)
possible_Word_Set = set()

#print(sorted(guessed_Word_Set))

while True:

    possible_letter = input("Enter possible letter: ")
    if possible_letter == chr(27).encode():
        if input(':') == 'quit':
            break
    if isletter(possible_letter) != 0:
        if ispart(possible_letter) != 0:
            print('The letter \'' + possible_letter + '\' is in the word')
            possible_Word_Set.add(possible_letter)
            if possible_Word_Set == guessed_Word_Set:
                print('You won! The word is ' + guessed_Word)
                break
            #print(sorted(guessed_Word_Set))
            #print(sorted(possible_Word_Set))
        else:
            print("Keep trying")
