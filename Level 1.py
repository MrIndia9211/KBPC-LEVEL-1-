def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    print("-------------------------")
    print("HI WELCOME TO KBPC Level 1[Kaun Bnega Profecitional Coder]")

    print("In This KBPC KBPC Level 1 WE ask some question from you Related to Programing or Computer languages")
    print("THIS KBPC IS MADE BY ![RAGHAV MALIK]!")
    for key in questions:

        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {

 "1.Which one is not a computer Language: ": "D",
 "2.Which language is used for styling in websites: ": "B",
 "3.What is full Form of html: ": "C",
 "4.What is the full form of css?: ": "A"
}

options = [["A. Html", "B. Ruby", "C. Python", "D. Jsom"],
          ["A. C++", "B. Css", "C. Styso", "D. Styler"],
          ["A.Hypertext Makeup language", "B. Hypertext Manual language", "C.Hypertext Markup Language", "D. Hamer tamer mono language"],
          ["A. Cascading Style Sheets","B. Cascading Song Sheets", "C. catch song series", "D. NONE OF THESE"]]

new_game()

while play_again():
    new_game()

print("Ok Byee Thanks for playing 👋")


# CODE BY CODER RAGHAV MALIK