import random

#Lady hunter tiger
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer choose l
    elif comp == 'l':
        if you=='h':
            return False
        elif you=='t':
            return True
    
    # Check for all possibilities when computer choose h
    elif comp == 'h':
        if you=='t':
            return False
        elif you=='l':
            return True
    
    # Check for all possibilities when computer choose t
    elif comp == 't':
        if you=='l':
            return False
        elif you=='h':
            return True

print("Comp Turn: Lady(l) Hunter(h) or Tiger(t)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'l'
elif randNo == 2:
    comp = 'h'
elif randNo == 3:
    comp = 't'

you = input("Your Turn: Lady(l) Hunter(h) or Tiger(t)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
