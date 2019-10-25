import random

words = ["overflow","rocks","book","keep","cool"]
word = random.choice(words)
print("Welcome to the Hangman")
guesses= int(input("Choose between 7 to 10 guesses: "))

print(word)
chars = []
for c in word:
    chars.append(c)

def win(c):
    if len(c) ==0:
        return True
    else:
        return False

result = False
while(guesses > 0):
    choice = input("Guess a letter: ")
    if choice in chars:
        chars.remove(choice)
        print("Correct! Guess another letter")
        guesses-=1
    else:
        print("Oops,try again")
        guesses-=1
    
    result = win(chars)
    if result == True:
        break

if result == True:
    print("You have won the game")
else:
    print("Sorry, you have lost the game")