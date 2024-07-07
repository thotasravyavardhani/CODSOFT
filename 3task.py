import random,string
# Get user input for the desired password length 
print(" \n\n Welcome to Password Generator !!! ")
while True: #Infinite loop : Until user satisfied with the password
    print("\n\nExit : ctrl + Enter") #To exit from terminal
    while True: #Infinite loop : Until user entered correct length of password
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.") #Exception Handling when we use string instead of integer or any other value errors
    
    # Define character sets for the password
    lower = string.ascii_lowercase#a,b,c,d,e...
    upper = string.ascii_uppercase#A,B,C,D,E,F....
    digits = string.digits#0,1,2,3...
    special = string.punctuation#$,@....

    # Combine all character sets
    all_chars = lower + digits + special+upper
    # Generate the password
    password = ''.join(random.choice(all_chars) for i in range(length))

    # Display the generated password
    print("\n \n Generated password: ",password)
    print("\n Do you want me to generate another password : (Yes/No) : ")
    s=input()
    if s== "No" or s=="no" or s=="NO":
        exit()