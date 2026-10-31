# Ask the user how many rows they would like
rows = int(input("How many rows would you like? "))

# Ask the user how many columns they would like
columns = int(input("How many columns would you like? "))

# Repeat once for each row
for row in range(rows):

# Print an ascii emoji for each column
    for column in range(columns):
        print(":-)", end=" ")

 # Move to a new line after each row is complete
    print()