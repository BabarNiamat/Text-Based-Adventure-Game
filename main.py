def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the left and right.")
    choice = input("Do you want to go left or right? ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        intro()

def left_path():
    print("You encounter a wild animal!")
    choice = input("Do you want to fight or flee? ").lower()
    if choice == "fight":
        print("You bravely fight the animal and win!")
        # Add more story here
    elif choice == "flee":
        print("You run away safely but feel like a coward.")
        # Add more story here
    else:
        print("Invalid choice. Please choose 'fight' or 'flee'.")
        left_path()

def right_path():
    print("You find a treasure chest!")
    choice = input("Do you want to open it or leave it? ").lower()
    if choice == "open":
        print("You find gold and jewels! You win!")
        # Add more story here
    elif choice == "leave":
        print("You walk away, wondering what could have been.")
        # Add more story here
    else:
        print("Invalid choice. Please choose 'open' or 'leave'.")
        right_path()

def main():
    intro()

if __name__ == "__main__":
    main()
