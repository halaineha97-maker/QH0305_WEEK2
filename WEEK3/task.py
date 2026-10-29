
# print(f"All required apples removed {value}")


#Ask the user how many bar should be charged
bars= int(input("How many bars should I charge? \n"))

#Initialise counter to zero
charged_bars = 0
while charged_bars < bars:
    print("charging.")
    #Increment the number of charged bars
    charged_bars = charged_bars + 1
    print(charged_bars)

print(f"The battery is fully charged {charged_bars}.")