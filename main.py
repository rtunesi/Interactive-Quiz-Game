# main coding file for the quiz game

def getAnswer():
    user_input = str(input("Please enter your answer: "))
    return user_input


def printQuestion(question):
    print(question)


def main():
    print("Hello world!")
    printQuestion("What is the size of the sun?")
    print(getAnswer())



if __name__ == "__main__":
    main()