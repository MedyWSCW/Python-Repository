

import random
GOOD_COMMENTS = ["Amazing!", "Keep it up!", "Fantastic!"]
BAD_COMMENTS = ["How bad can you be!", "Keep trying", "You are horrible!"]
QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D."
QUESTIONS = ["What is spidermans real name?",
               "Which of these charatcers isnt a batman villian?",
                "What city does miles morales live in?"]
OPTIONS = [["Peter Parker","Bruce Banner","Tony Stark","Steve Rogers"],
                   ["Joker","Scarecrow","Loki","Penguin"],
                   ["Seattle","Brooklyn","Chicago","Portland"]]
SHORT_OPTIONS = ["a","b","c","d"]
ANSWERS = [0, 2, 1]
play = "yes"

QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "


# Ask the user their name and store it
name = input ("What is your Name? ")
if name == "Daequan":
    print("Its a Monkey!")
    print("I never knew a monkey would play this quiz.")

if name == "James":
    print("Its the guy with the massive forehead!")
    print("you better use that massive forehead for this quiz.")

#Greet the user and introduce the quiz
print ( "Welcome to this quiz",name)
print ( "This quiz is about Superheros")

#Check number of qestion atempts 
while True:
 try:

   tries= input("How many attempts would you like at each question 1-4? ")
   tries= int(tries)
   break 
 except:
    print ("That's not a number")

#while play
while play == "yes":
    score = 0
    for i in range(len(QUESTIONS)):
        question_atempts = tries
        while question_atempts > 0:
            #Ask the user a question
            
            answer = input (QUESTION_FORMAT.format(QUESTIONS[i],OPTIONS[i][0],
                                                    OPTIONS[i][1], OPTIONS[i][2],OPTIONS[i][3])).lower()
            
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print ("Correct! you got 5 points.")
                score += 5
                print(random.choice(GOOD_COMMENTS))
                break

            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print ("Wrong!")
                print(random.choice (BAD_COMMENTS))
            
            else:
                print("That was not a option")

    #End the quiz
    print ("Well done {}. That's the end. Your final score is {}".format (name,score ))
    print ("Thanks for playing!")

     #Replay
    play = input("Do you want to play again?").lower()
    print("Goodbye")
