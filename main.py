# main coding file for the quiz game

def getAnswer():
    user_input = str(input("Please enter your answer: "))
    return user_input


def printQuestion(question):
    print(question)


print("Hello world!")
printQuestion("What is the size of the sun?")
print(getAnswer())