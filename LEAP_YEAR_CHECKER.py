while True:
    # Prompt the user to input a year
    year = int(input("Enter a year: "))

    # Leap year logic using nested if statements
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year.")
        else:
            print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

    another = input("Do you want to check another year? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Goodbye!")
        break
