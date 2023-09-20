the_name = "Jonh"

while True:  # Do while
    print("Try to guess the name: ")
    name = input("Whats your name?: ")
    if name == the_name:
        print("Correct name.")
        break
    else:
        print("Incorrect answer.")

else:
    print("Aplication error")
