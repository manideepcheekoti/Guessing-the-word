import random
words = ["apples", "oracle", 'amazon', 'microsoft', 'orange', 'cat', 'dog']
guessed_word = random.choice(words)
hint = guessed_word[0]+guessed_word[-1]

store_g_l = []
try_p = 6
a = input("Enter ur name:")
print(f"""Hello {a}.
Welcome to the game.""")
print("We are going to give u 6 attempts for guessing.")

for guess in range(try_p):
    while True:
        letter = input('Guess the letter:')
        if len(letter) == 1:
            break
        else:
            print("Oops! Please guesss a letter")
    if letter in guessed_word:
        print("yes")
        store_g_l.append(letter)
    else:
        print("no")

    if guess == 3:
        clue_request = input("Would u like a clue?  y/n")
        if clue_request == "y":
            print(f"CLUE:The first and last letters of the word is {hint}")
        else:
            print("You're very confident")

print(f"Now lets see what u have guessed so far.You have guessed {len(store_g_l)} letters correctly.")
print(store_g_l)
word_guess = input("Guess the word:")
if word_guess == guessed_word:
    print("Congrats! u r correct.")
else:
    print(f"Sorry! The answer is {guessed_word}")








