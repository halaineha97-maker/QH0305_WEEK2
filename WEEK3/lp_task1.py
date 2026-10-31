#display message
brightness = int(input("what level of brightness is required?\n"))
print("\n Adjusting brightness..\n")
#generate even numbers from 2 to the chosen brightness

for level in range(2, brightness+1,2):
    print("*" * level)

print("\n Complete")