import random
def win(comp,me):
    if comp==me:
        return None
    elif comp=='c':
        if me=='z':
            return True 
        elif me=='c':
            if comp=='c':
                return False
print("Comp Turn : Cross(c)  or Zero(z)?")            
radNo=random.randint(1,2)
if radNo==1:
    comp='c'
elif radNo==2:
    comp='z'

me=input("Now It's Time For My Turn : Cross(c) or Zero(z)")
a=win(comp,me)
print(f"Computer choose {comp}")
print(f"I choose {me}")
if a==None:
    print("The game is tie !")
elif a:
    print("You Win")
else:
    print("You Lose !!")            


    
    