#Display the initial message
print("Program Started!")
#Display the second message
print("Please enter a standard character:")
#Read the users input
letter = input()

#Check that exact one character was entered
if len(letter) == 1:

#Find the ASCII code of the letter
    value = ord(letter)
#Display the result
    print(f"The ASCII code for {letter} is {value}.")
else:
# Display an error message if more than one character was entered
    print("Error: Haha! enter one letter fool.")

# Display an end message
print("Program Ended!")
