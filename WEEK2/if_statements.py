# # Ask the user the type of book
# book_type = input("What type of book is this?")
#
# if book_type == "Adventure":
#     print("I like adventure books!")
#
# print("Finished reading book.")
#

# # Ask the user to instruct for direction first
# direction = input("Towards which direction should I go (Up, Down,Left, Right):")
#
# if direction  == 'Up':
#     print("I am moving in an upward direction!")
# elif direction  == 'Down':
#     print("I am moving in a downward direction!")
# elif direction  == 'Left':
#     print("I am moving in a left direction!")
# else:
#     print("I am moving in a right direction!")


# ask user what cover of the book
print("What type of cover of the book (hard/soft)?")
cover = input()
if cover == 'soft':
    print("Is the book perfect-bound (yes/no)?")
    bound = input()
    if bound == 'yes':
    print("soft cover, perfect bond are very popular")
    else:
    print("soft cover with coils or stiches are great for short books")
elif cover == 'hard':
    print("Book with hard cover can be expensive!")