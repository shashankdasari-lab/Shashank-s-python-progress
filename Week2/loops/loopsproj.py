play_again = "Y"

while play_again == "Y":

    print("WELCOME TO PYTHON QUIZ\n")

    name = input("Enter your name: ")

    print("")
    print("QUIZ GAME RULES")
    print("")
    print("1. The quiz contains 3 multiple-choice questions.")
    print("2. Each question has 4 options: A, B, C and D.")
    print("3. Enter only the option letter (A/B/C/D).")
    print("4. Each correct answer awards 1 mark.")
    print("5. There is no negative marking for wrong answers.")
    print("6. Once an answer is submitted, it cannot be changed.")
    print("7. The final score and percentage will be displayed at the end of the quiz.")
    print("8. Try to answer all questions without guessing!\n")

    # Reset score every time the quiz starts
    score = 0
    correct = 0
    wrong = 0

    print("\nQ1. Which keyword is used to define a function in Python?")
    print("A. function")
    print("B. define")
    print("C. def")
    print("D. func")

    first = input("Enter your preferred option: ").upper()

    if first == "C":
        print("Correct Answer! 1 point awarded.")
        score += 1
        correct += 1
    elif first == "A" or first == "B" or first == "D":
        print("Wrong Answer!")
        wrong += 1
    else:
        print("Invalid Option!")

    print("Current Score:", score)

    
    print("\nQ2. Which loop is generally used when the number of iterations is known?")
    print("A. while")
    print("B. for")
    print("C. repeat")
    print("D. do-while")

    second = input("Enter your preferred option: ").upper()

    if second == "B":
        print("Correct Answer! 1 point awarded.")
        score += 1
        correct += 1
    elif second == "A" or second == "C" or second == "D":
        print("Wrong Answer!")
        wrong += 1
    else:
        print("Invalid Option!")

    print("Current Score:", score)

  
    print("\nQ3. Which of the following is a mutable data type in Python?")
    print("A. Tuple")
    print("B. String")
    print("C. List")
    print("D. Integer")

    third = input("Enter your preferred option: ").upper()

    if third == "C":
        print("Correct Answer! 1 point awarded.")
        score += 1
        correct += 1
    elif third == "A" or third == "B" or third == "D":
        print("Wrong Answer!")
        wrong += 1
    else:
        print("Invalid Option!")

    print("Current Score:", score)

   
  
    print(" QUIZ RESULTS")
   

    print("Player Name      :", name)
    print("Total Questions  :", 3)
    print("Correct Answers  :", correct)
    print("Wrong Answers    :", wrong)
    print("Final Score      :", score)
    print("Percentage       :", (score / 3) * 100, "%")

    
    play_again = input("\nDo you want to play again? (Y/N): ").upper()

print("\nThanks for playing! ")