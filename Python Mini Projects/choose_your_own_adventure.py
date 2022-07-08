name = input("Type your name: ")
print("Welcome,", name, "to this wonderous adventure!")

answer = input("You are on a dimly lit path, it has come to an end and you can go left or right. Which way would you like to go? Type left to go left, right to go right. ").lower()

if answer == "left":
    answer = input("You come to a river with a bridge lit with lanterns, you can simply cross the bridge, or swim across? Type walk to cross the bridge, or swim to swim across: ")
    
    if answer == "walk":
        print("Such a simple option, you didn't think it would be that easy did you? A band of wild boar rush from the woods across the bridge and gore you with their tusks...You Died.")
    elif answer == "swim":
        print("The waters seemed raging, but it was a trick of your eyes, you start to swim across but something grabs onto your leg! An anaconda grips around you while squeezing tightly and takes you under...You Died.")
    else:
        print("FOOL! Stick with the choices before you, lest your adventure end short! You Died.")  
    
elif answer == "right":
    answer = input("You walk for a few miles and come to a town, there's an inn to the left and a bar to the right, where do you go? Type left for inn, and right for bar. ")
    
    if answer == "left":
        print("You go to the inn to rest after your arduous journey, inside you're greeted by a sweet innkeeper. You awaken in a bath full of ice, the innkeeper has harvested your kidneys...You Died.")
    elif answer == "right":
        answer = input("Inside, the bar is bustling, but you notice a lone hooded stranger in the corner, do you approach, or go to the bar for a drink? Type approach to interact with the stranger, or bar to get a drink. ")
        
        if answer == "approach":
            print("You approach the hooded loner in the corner and he gestures for you to sit, he then tells you the lore of the land and its curse, how if you'd approached anyone other than him, they'd have their motives for killing you, but instead you talk for hours with the stranger and he gives you gold and safe passage...Congratulations! You WIN! ")
            
        elif answer == "bar":
            print("You sit at the bar and order a drink of local origin, after about five minutes of conversing with the locals around you and the bartender, you start to feel funny, the bartender has poisoned your drink...You Died.")

        else:
            print("FOOL! Stick with the choices before you, lest your adventure end short! You Died.")

    else:
        print("FOOL! Stick with the choices before you, lest your adventure end short! You Died.")

else:
    print("FOOL! Stick with the choices before you, lest your adventure end short! You Died.")

print("Thank you for playing", name + "!")