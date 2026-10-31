#display the initial message
print("What phrase do you want to see in reverse?")
#ask the user for the input
phrase = input()
print("Reversing...")
# Loop through the phrase from the last character to the first
for i in range(len(phrase) - 1, -1, -1):
    print(phrase[i], end="")
