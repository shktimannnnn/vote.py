try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are valid to vote")
    else:
        print("You are not valid to vote")

except ValueError:
    print("Enter a valid integer")
