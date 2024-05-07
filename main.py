score = 0
# Ask the user their name and store it
name = input ("What is your Name? ")
 #Greet the user and introduce the quiz
print ( "Welcome to this quiz",name)
print ( "This quiz is about Superheros")
 #Ask the user a question
answer = input ( "What is spidermans real name? " ).lower()
if answer == "Peter Parker".lower():
 print ("Correct! you got 5 points.")
 score += 5
elif answer == "":
 print ("Not sure?")
else:
 print("Incorrect")
 #Tell them the correct answer
print ("The answer is Peter Parker")
 #End the quiz
print ("Well done. That's the end. You got ",score, "points")
print ("Thanks for playing!")

