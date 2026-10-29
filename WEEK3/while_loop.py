#Ask the user how many apples to remove
User_input= input("How many apples should I remove?\n")

#Initialise counter to zero
value = 0

while value < int(User_input):
    print("Remove Apple")
    value = value+1

print(f"All required apples removed {value}")
