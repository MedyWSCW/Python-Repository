

import random
GOOD_COMMENTS = ["Amazing!", "Keep it up!", "Fantastic!"]
BAD_COMMENTS = ["How bad can you be!", "Keep trying", "You are horrible!"]

play = "yes"
QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "


# Ask the user their name and store it
name = input ("What is your Name? ")


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

    question_atempts = tries
    while question_atempts > 0:
        score = 0
        #Ask the user a question
        question1 = "What is spidermans real name? "
        a = "Peter Parker"
        b = "Bruce Banner"
        c = "Tony Stark"
        d = "Steve Rogers"
        answer = input (QUESTION_FORMAT.format(question1, a, b, c, d)).lower()
        if answer == a or answer == "a":
            print ("Correct! you got 5 points.")
            score += 5
            print(random.choice (GOOD_COMMENTS))
            break
        elif answer == "":
            print ("Not sure?")
        elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print ("That wasnt an option")
        else:
            print("Incorrect")
            print(random.choice (BAD_COMMENTS))

        
    #Tell them the correct answer
        question_atempts -=1
    print ("The answer is Peter Parker")

    #while play
    
    question_atempts = tries
    while question_atempts > 0:
        #Ask the user a question
        question2 = "Which of these charatcers isnt a batman villian? ".lower()
        a = "Joker"
        b = "Scarecrow"
        c = "Loki"
        d = "Penguin"
        answer = input (QUESTION_FORMAT.format(question2, a, b, c, d)).lower()
        if answer == c or answer == "c":
            print ("Correct! you got 5 points.")
            score += 5
            print(random.choice (GOOD_COMMENTS))
            break
        elif answer == "":
            print ("Not sure?")
        elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print ("That wasnt an option")
        else:
            print("Incorrect")
            print(random.choice (BAD_COMMENTS))
                
        #Tell them the correct answer
        question_atempts -=1
    print ("The answer is Loki")

    question_atempts = tries
    while question_atempts > 0:

        question3 = "What city does miles morales live in?".lower()
        a = "Seattle"
        b = "Brooklyn"
        c = "Chicago"
        d = "Portland"
        answer = input (QUESTION_FORMAT.format(question3, a, b, c, d)).lower()
        if answer == b or answer == "b":
            print ("Correct! you got 5 points.")
            score += 5
            print(random.choice (GOOD_COMMENTS))
            break
        elif answer == "":
            print ("Not sure?")
        elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
                print ("That wasnt an option")
        else:
            print("Incorrect")
            print(random.choice (BAD_COMMENTS))

        #Tell them the correct answer
        question_atempts1 -=1
        print ("The answer is Brooklyn")

    #End the quiz
    print ("Well done {}. That's the end. Your final score is {}".format (name,score ))
    print ("Thanks for playing!")

     #Replay
    play = input("Do you want to play again?").lower()
    print("Goodbye")
