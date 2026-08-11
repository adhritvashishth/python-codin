import random
words=input("enter a word")
secret_word=words
guessed_letters=[]
lives=6
print(" WELCOME TO HANGMAN")
while lives>0:
    display_word=""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word+=letter+" "
        else:
            display_word+="_ "
    print("\nWord to guess: "+display_word)
    print(f"Lives remaining: {lives}")
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word and won!₹")
        break
    guess=input("Guess a letter: ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter exactly one single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter! Try a different one.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Good job! That letter is in the word.")
    else:
        print("Oops! That letter is not in the word.")
        lives-=1
if lives==0:
    print(f"\nGame Over! You ran out of lives. The word was: {secret_word}")