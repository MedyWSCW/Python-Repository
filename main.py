
play = "yes"
QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "


# Ask the user their name and store it
name = input ("What is your Name? ")


#Greet the user and introduce the quiz
print ( "Welcome to this quiz",name)
print ( "This quiz is about Superheros")

#Check number of qestion atempts 
tries= input("How many attempts would you like at each question 1-4? ")
tries= int(tries)
print("")

#while play
while play == "yes":
    score = 0


    #Ask the user a question
    question = "What is spidermans real name? "
    a = "Peter Parker"
    b = "Bruce Banner"
    c = "Tony Stark"
    d = "Steve Rogers"
    answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == a or answer == "a":
        print ("Correct! you got 5 points.")
        score += 5
    elif answer == "":
        print ("Not sure?")
    elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print ("That wasnt an option")
    else:
        print("Incorrect")

        
    #Tell them the correct answer
    print ("The answer is Peter Parker")


    #Ask the user a question
    question = "Which of these charatcers isnt a batman villian? ".lower()
    a = "Joker"
    b = "Scarecrow"
    c = "Loki"
    d = "Penguin"
    answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == c or answer == "c":
        print ("Correct! you got 5 points.")
        score += 5
    elif answer == "":
        print ("Not sure?")
    elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print ("That wasnt an option")
    else:
        print("Incorrect")
        


    #Tell them the correct answer
    print ("The answer is Loki")
    question = "What city does miles morales live in?".lower()
    a = "Seattle"
    b = "Brooklyn"
    c = "Chicago"
    d = "Portland"
    answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == b or answer == "b":
        print ("Correct! you got 5 points.")
        score += 5
    elif answer == "":
        print ("Not sure?")
    elif  answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print ("That wasnt an option")
    else:
     print("Incorrect")


    #Tell them the correct answer
    print ("The answer is Brooklyn")

    #End the quiz
    print ("Well done {}. That's the end. Your final score is {}".format (name,score ))
    print ("Thanks for playing!")


    #Replay
    score = 0
    play = input("Do you want to play again?").lower()

print("Goodbye")
