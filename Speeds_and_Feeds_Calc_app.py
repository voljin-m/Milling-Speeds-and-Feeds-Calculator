import Functions_and_Classes

print("Welcome to the Milling Speeds and Feeds Calculator!")

while True:
    print("Please choose what to calculate: \n 1) Surface Speed \n 2) Spindle Speed \n 3) Feeds \n 4) Exit Calculator")
    user_choice = int(input("Enter Your choice: "))

    if user_choice == 1:
        Functions_and_Classes.Surface_Speed()
    elif user_choice == 2:
        Functions_and_Classes.Spindle_Speed()
    elif user_choice == 3:
        Functions_and_Classes.Feed_Choice()
    elif user_choice == 4:
        print("Thank You for using this Calculator! Goodbye!\n\n")
        break
    else:
        print("You choice is invalid!")
    Another_Calculation = input("Do You want to use this Calculator again? (y/n): ")
    if Another_Calculation == "Y" or Another_Calculation == "y":
        continue
    else:
        print("Thank You for using this Calculator! Goodbye!\n\n")
        break

wait = input("Press enter to exit.")
