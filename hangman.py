word = (f"i have a Secret")

allowed_errers = 13
guesses = []
done = False



while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    
    
    guess = input(f"Allowed Erreors Left {allowed_errers}, Next Guess:  ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errers -= 1
        if allowed_errers == 0:
            break
        
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
            
if done:
    print(f"you found the word! it was {word}!")
else:
    print(f"Game Over! the word was {word}!")