import random
secret_words = ["apple", "mango", "python", "javascript", "grapes"]
chosen_word = random.choice(secret_words)
display_word= ["_"] * len(chosen_word)
lives_remaining = 6
letters_tried = []

print("=== MY HANGMAN GAME ===")
print("Guess the word letter by letter")

while lives_remaining > 0 and "_" in display_word:
    print("\nCurrent word: ", " ".join(display_word))
    print(f"Lives left: {lives_remaining}")
    print(f"Letters used: {', '.join(letters_tried)}")

    player_guess = input("Type a letter: ").lower()

    if len(player_guess)!= 1 or not player_guess.isalpha():
        print("Enter only a single letter")
        continue

    if player_guess in letters_tried:
        print("You already used that letter")
        continue

    letters_tried.append(player_guess)

    if player_guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == player_guess:
                display_word[index] = player_guess
        print("Correct!")
    else:
        lives_remaining -= 1
        print("Wrong guess!")

if "_" not in display_word:
    print(f"\nYou won! The word was: {chosen_word}")
else:
    print(f"\nYou lost! The word was: {chosen_word}")