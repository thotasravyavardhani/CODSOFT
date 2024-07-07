def oper(ch):
    if ch==1:
        return '+'
    elif ch==2:
        return '-'
    elif ch==3:
        return 'x'
    elif ch==4:
        return '/'
    elif ch==5:
        return '^'

print("\n\n ",'-'*15,'Welcome to Calculator!!!!','-'*15)

#Displaying choice of basic Arthimetic Operations
i=1
while(1):
    print("\n\n")
    print("Exit : ctrl + Enter \n\n")
    n1=int(input("Enter First Number: "))
    print()
    n2=int(input("Enter Second Number: "))
    print("\n\n")
    print(i,"Basic Arthimetic Operations are: ")
    print("   choics 1.Addition : +")
    print("   choics 2.Subtraction : -")
    print("   choics 1.Multiplication : X")
    print("   choics 4.Division : /")
    print("   choics 5.Power or Exponential : ^")
    print("If you want to EXIT press ctrl + Enter (or) as choice 6")
    print()
    i+=1
    choice=int(input("Enter your hoice (In Integer value) : "))
    if choice in [1,2,3,4,5]:
        if choice==1:
            f=n1+n2
        elif choice==2:
            f=n1-n2
        elif choice==3:
            f=n1*n2
        elif choice==4:
            f=n1/n2
        elif choice==5:
            f=n1^n2
    elif choice==6:
        s=input('\n\n Are you sure you want to EXIT? - Yes / No \n\n')
        if s=='yes' or s=='Yes' or s=='YES':
            exit()
        else:
            print("!! Enter correct choice  !!")
            continue
        r=str(n1)+" "+oper(choice)+" "+str(n2)
        print('\n')
        print('-'*20)
        print("Operation : ",r)
        print("Final Result : ",f)

        
    
