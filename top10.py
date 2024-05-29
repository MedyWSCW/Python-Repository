#----FUNCTIONS---
guesses = []
MUSIC_ARTIST_ANSWERS = ["the weeknd", "taylor swift", "post malone", "rihanna", 
                        "ariana grande", "billie eilish", "drake", "dua lipa", 
                        "kendrick lamar", "justin bieber"]

# Welcome the user and introduce the quiz
def intro():
    # Ask the user their name 
    name = input("What is your name? ")
    # Greet the user and introduce the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is about music artists. Can you guess the person by the hint?")

# Ask the user for lives and confirm it's valid
def getLives():
    while True:
        lives = input("How many chances do you want? ")
        try:
            # Check if it's a valid number 
            lives = int(lives)
            if lives > 0:
                return lives
            else:
                print("Please pick a positive number greater than zero.")
        except ValueError:
            print("That's not a number. Please enter a valid number.")

# Check if the answer already exists in the list. Used for checking both correct answers and previous guesses.
def inList(answer, list):
    return answer in list

# --- MAIN CODE ---
intro()
lives = getLives()
score = 0

# Begin quiz 
while lives > 0:
    answer = input("Name one of the top 10 artists with the most monthly listeners:\n").lower()
    
    # Check if correct or wrong
    if inList(answer, MUSIC_ARTIST_ANSWERS):
        # Check if already guessed or not    
        if inList(answer, guesses):
            print("You've guessed that already.")
        else:
            print("Correct!")
            score += 5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining.".format(len(guesses), score, lives))
    else:
        print("Wrong.")
        lives -= 1
        print("You have guessed {}. Your score is {}. You have {} chances remaining.".format(len(guesses), score, lives))

    
    if score == 50:
        print("Congrats, you have correctly guessed all the answers.")
        break
# End Game
print("Game Over. Your final score was {}.".format(score))