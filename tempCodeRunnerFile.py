import random

def choose_word_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return random.choice(words)

word_file_path = "C:/Users/NoNam/Downloads/words.txt"

max_guesses = 6
letters_guessed = []
player_name = ""

def guess_status():
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "
    return guessed_word.strip()

def print_guessed():
    incorrect_guesses = [letter for letter in letters_guessed if letter not in secret_word]
    if incorrect_guesses:
        return "[" + ", ".join(incorrect_guesses) + "]"
    else:
        return "[]"

def print_status(lives):
    print("Name:", player_name)
    print(guess_status() + "\t " + print_guessed() + "\t Lives:", lives)

def play_game(lives):
    print_status(lives)
    while lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in letters_guessed:
            print("You already guessed that letter!")
            continue
        letters_guessed.append(guess)
        if guess not in secret_word:
            print("Incorrect guess!")
            lives -= 1
        if all(letter in letters_guessed for letter in secret_word):
            print(guess_status() + "\t " + print_guessed() + "\t Winner")
            break
        print_status(lives)
    else:
        print(secret_word + "\t " + print_guessed() + "\t Lost")

def main():
    global letters_guessed, player_name, secret_word
    player_name = input("Enter your Name: ")
    play_again = "y"
    while play_again.lower() == "y":
        secret_word = choose_word_from_file(word_file_path)
        letters_guessed = []
        play_game(max_guesses)
        play_again = input("Do you want to play again? (y/n): ")
        
if __name__ == "__main__":
    main()
