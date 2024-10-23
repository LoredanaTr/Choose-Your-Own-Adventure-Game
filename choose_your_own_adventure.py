# Start of the adventure game for kids with princes and princesses

name = input("What is your name, little princess or brave prince? ")
print("Welcome to the magical kingdom,", name, "where a great adventure awaits you!")

answer = input(
    "You are on a magical path that leads to a beautiful castle, but the road splits. "
    "You can go left to the Enchanted Forest or right to the Rainbow Bridge. "
    "Which way would you like to go? (left/right): ").lower()

if answer == "left":
    answer = input("You have reached a sparkling lake. You can walk around it or fly over it with your magical wings. "
                   "What do you choose? Type 'walk' to walk around or 'fly' to fly over: ").lower()
    if answer == "fly":
        print("You fly gracefully over the lake with your magical wings and land safely on the other side. Well done!")
        answer = input("On the other side, you meet a talking tree who offers you two paths: "
                       "'climb' to climb the tree and see the stars, or 'continue' to walk further into the forest. "
                       "What do you choose? (climb/continue): ").lower()
        if answer == "climb":
            print("You climb the magical tree and get to see a beautiful view of the entire kingdom, "
                  "shining under the stars!")
            print("The tree thanks you for your kindness and gives you a magical fruit that grants you a wish. "
                  "You win!")
        elif answer == "continue":
            print("You continue walking through the forest and discover a hidden treasure chest full of"
                  " sparkling jewels!")
            print("You are now the owner of the treasure! Congratulations, you win!")
        else:
            print("That is not a valid option. You lose the adventure.")
    elif answer == "walk":
        print("You walked around the lake, but got lost among the trees. "
              "You find yourself in front of a mystical cave.")
        answer = input("Do you want to enter the cave or try to find your way out of the forest? "
                       "Type 'enter' to explore the cave or 'exit' to leave the forest: ").lower()
        if answer == "enter":
            print("You enter the cave and find a sleeping dragon guarding a mountain of gold!"
                  " You tiptoe quietly and escape with some treasure!")
            print("You made it back safely with treasure. You win!")
        elif answer == "exit":
            print("You manage to find your way out of the forest and safely return to the castle.")
            print("The King and Queen welcome you back to the castle with a royal feast! You win!")
        else:
            print("That is not a valid option. You lose the adventure.")
    else:
        print("That is not a valid option. You lose the adventure.")

elif answer == "right":
    answer = input("You arrive at the Rainbow Bridge. It looks a bit shaky. Do you want to cross it or go back? "
                   "Type 'cross' to cross the bridge or 'back' to return: ").lower()
    if answer == "back":
        print("You decided to go back and missed the magical adventure. You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a friendly unicorn. "
                       "Do you want to talk to the unicorn? (yes/no): ").lower()
        if answer == "yes":
            print("You talk to the unicorn, and it gives you a magical gift of sparkling diamonds!")
            answer = input("The unicorn also tells you about a hidden garden full of beautiful flowers. "
                           "Do you want to visit the garden or continue to the castle? (garden/castle): ").lower()
            if answer == "garden":
                print("You visit the hidden garden and find a magical flower that grants wishes. "
                      "You make a wish and it comes true!")
                print("Congratulations! You win!")
            elif answer == "castle":
                print("You continue to the castle, where the King and Queen welcome you to a grand royal ball!")
                print("You are the guest of honor at the royal ball! You win!")
            else:
                print("That is not a valid option. You lose the adventure.")
        elif answer == "no":
            print("You chose not to talk to the unicorn, and it flies away. You missed a magical moment!")
            print("Unfortunately, you lose the adventure.")
        else:
            print("That is not a valid option. You lose the adventure.")
    else:
        print("That is not a valid option. You lose the adventure.")

else:
    print("That is not a valid option. You lose the adventure.")

