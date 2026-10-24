# ask user where to look
print("Where should I look?")
location =input()

if location == "in the bedroom":
    print("where in the bedroom should I look?")
    place = input()

    if place =="under the bed":
        print("Found some shoes but no phone.")
    else:
        print("Found some mess but no phone.")

elif location == "in the bathroom":
    print("The bathroom should I look?")
    place = input()

    if place =="in the bathtub":
        print("Found some rubber duck but no phone.")
    else:
        print("Found bathroom stuff but no phone.")

elif location == "in the living room":
    print("The living room should I look?")
    place = input()

    if place =="on the table":
        print("Yes I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    print("I don't know where that is but I will keep looking")

