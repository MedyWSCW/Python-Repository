# Ask the user their name and store it
name = input ("What is your Name? ")
 #Greet the user and introduce the quiz
print ( "Welcome to this quiz",name)
print ( "This quiz is about Superheros")
 #Ask the user a question
answer = input ( "What is spidermans real name? " )
if answer == "Peter Parker":
 print ("Correct")
elif answer == "":
 print ("Not sure?")
else:
 print("Incorrect")
 #Tell them the correct answer
print ("The answer is Peter Parker")
 #End the quiz
print ("Thanks for playing!")

