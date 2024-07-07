import random
s=0
print("--------------------------Let's Start Game--------------------------")
i=0
comp=0
while(1):
    i+=1
    print("\n\n")
    print('-----------Round - ',i,'-------------')
    n=int(input(" 1. Rock \n 2. paper\n 3. Scissor\n Enter your choice : "))
    co=random.randint(1,3) 
    if n>3 or n<1:
        print("Invalid Input")
        continue
    elif n==co:
        print(" Computer choice :",co)
        print("************** Tie ******************\n")
    elif n==1 and co==2 or n==2 and co==3 or n==3 and co==1:
        print(" Computer choice :",co)
        print("*********   You Lose - try Again  ******************\n")
        comp+=1
    else:
        print(" Computer choice :",co)
        print("******** You Win Hey congrats--- Its Party Time *************\n")
        s+=1
    print("\n-------------------------------------------------------------------\n")
    print("Round : ",i)
    print("Final Score : (Upto now) :")
    print("Your Score : ",s)
    print("Computer Score : ",comp)
    c=0
    while(1):
        ch=int(input("\n\n 1.Another Game\n 2.Exit\n Enter your choice: "))
        if ch==1:
            c=1
            break
        elif ch==2:
            print("-----------------------------------------------------------------")
            print("Thanks for Playing")
            print("Round : ",i)
            print("Final Score : ",s)
            print("Computer Final Score : ",comp)
            if s>comp:
                print("Congrats !! You had Won In this Game ")
            elif comp>s:
                print("Computer had won this game")
            else:
                print('Its Tie!!!!!')
            c=2
            break
        else:
            print("Invalid Input")
    if c==2:
        break

