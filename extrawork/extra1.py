try:
    marks1 = float(input("Enter your marks 1: "))
    if marks1 < 1 or marks1 > 100:
        print("Invalid input! Marks must be between 1 and 100.")
        exit()
    marks2 = float(input("Enter your marks 2: "))
    if marks2 < 1 or marks2 > 100:
        print("Invalid input! Marks must be between 1 and 100.")
        exit()
    marks3 = float(input("Enter your marks 3: "))
    if marks3 < 1 or marks3 > 100:
        print("Invalid input! Marks must be between 1 and 100.")
        exit()
    marks4 = float(input("Enter your marks 4: "))
    if marks4 < 1 or marks4 > 100:
        print("Invalid input! Marks must be between 1 and 100.")
        exit()
    marks5 = float(input("Enter your marks 5: "))
    if marks5 < 1 or marks5 > 100:
        print("Invalid input! Marks must be between 1 and 100.")
        exit()
    avg = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
    if avg >= 90:
        print("Very good! You got", avg, "%")
    elif avg >= 80:
        print("Good job! You got", avg, "%")
    elif avg >= 70:
        print("Good, can do better. You got", avg, "%")
    elif avg >= 60:
        print("You should study more. You only got", avg, "%")
    else:
        print("You failed. You got", avg, "%")
except ValueError:
    print("Invalid input! Please enter numbers only.")
