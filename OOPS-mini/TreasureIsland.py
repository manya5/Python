print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
direction = input("You're at a cross road. Where do you want to go?\n left or right: ")
option = input("Now, what you want to prefer?\n swim or wait: ")
door = input("Which door you prefer to go?\n red, yellow or blue: ")

if direction == "right":
    print("Game over")

if option == "swim":
    print("Game over")

if door == "red":
    print("Game over")

elif door == "blue":
    print("Game over")

else:
    print("Here is your Treasure!")
        