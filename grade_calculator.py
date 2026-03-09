while True:
    name = input("\nEnter student name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
        
    try:
        subject1 = float(input("Enter marks for subject 1: "))
        subject2 = float(input("Enter marks for subject 2: "))
        subject3 = float(input("Enter marks for subject 3: "))
        
        average = (subject1 + subject2 + subject3) / 3
        
        print("\n" + "-" * 30)
        print(f"Student Name: {name}\n")
        print(f"Average Marks: {average:.2f}\n")
        
        if average >= 75:
            print("Grade: A")
        elif average >= 60:
            print("Grade: B")
        elif average >= 40:
            print("Grade: C")
        else:
            print("Grade: Fail")
        print("-" * 30)
            
    except ValueError:
        print("\n" + "-" * 30)
        print("Error: Please enter valid numeric marks.")
        print("-" * 30)
