score = 0
# Ask the user their name and store it
name = input ("What is your Name? ")
 #Greet the user and introduce the quiz
print ( "Welcome to this quiz",name)
print ( "This quiz is about Superheros")
 #Ask the user a question
question = "What is spidermans real name? ".upper().lower()
a = "Peter Parker"
b = "Bruce Banner"
c = "Tony Stark"
d = "Steve Rogers"
answer = input ("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()
if answer == "A" or answer == "a":
 print ("Correct! you got 5 points.")
 score += 5
elif answer == "":
 print ("Not sure?")
else:
 print("Incorrect")
 #Tell them the correct answer
print ("The answer is Peter Parker")
 #End the quiz
print ("Well done {}. That's the end. Your final score is {}".format (name,score ))
print ("Thanks for playing!")

