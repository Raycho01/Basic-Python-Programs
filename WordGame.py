import random

word_list = ["handful", "candidate", "cholesterol", "dimension", "enforcement", "framework", "membership", "pursue", "rhythm", "smooth",]
lifes_amount = 5
number = random.randint(0,9)
single_word = word_list[number]

for cell in single_word:
    if cell == single_word[0] or cell == single_word[-1]:
        print(cell, end = " ")
    else:
        print("_", end = " ")

def char_compare(single_word, guess_char, result, lifes_amount):
    i = 0
    if(guess_char in single_word):
        for cell in single_word:
            if cell == guess_char:
                result[i] = cell
            else:
              pass
            i += 1

    else:
        lifes_amount -= 1
        print("This character is not in the word.")
    return result, lifes_amount

def guessed_or_not(single_word, result):
    i = 0
    for cell in single_word:
        if cell != result[i]:
            return 0
        i += 1
    return 1

result = []
for cell in single_word:
    if cell == single_word[0] or cell == single_word[-1]:
        result.append(cell)
    else:
        result.append("_")

while lifes_amount > 0:
    print("\nTake a guess: ")
    guess_char = input()

    if type(guess_char) == str:
        result, lifes_amount = char_compare(single_word, guess_char, result,lifes_amount)
        for cell in result:
            print(cell, end = " ")
        if guessed_or_not(single_word, result) == 1:
            break
        print("\nRemaining lifes: %s" %lifes_amount)

    else:
        print("Invalid input.")

if lifes_amount == 0:
    print("Game over. The word was: %s" %single_word)