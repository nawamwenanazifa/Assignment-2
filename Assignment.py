# The volume of a sphere with raduis r is (4/3)*pie*r**2
#what is the volume of a sphere with raduis 5
#make sure the programme enters the raduis from the key board and provide the answer in two decimal places

raduis=int(input("Enter the raduis of the sphere:"))
volume=(4/5)*22/7*raduis**2
print(f"the volume of a sphere with raduis{raduis} is {volume:.2f} cubic meters")

#create a programme to calculate the area of a triangle (1/2*base*height)
#base and height should be entered using a key board

base=int(input("Enter the base of a triangle"))
height=int(input("Enter the height of a triangle"))
area_of_a_triangle=(1/2*base*height)
print(f"the area of a triangle { area_of_a_triangle}")


#witu has tasked  you to automate a simple grading system
#as a python student , write a programme using to display the grades that the students will be be receiving based on the the marks scored
#The grades are:
#90% - 100%  Grade is A
#80% - 89%   Grade is B
#70% - 79%   Grade is C
#60% - 69%   Grade is D
#50% - 59%   Grade is E
#< 50% Fail



marks_scored=int(input("Enter the stundent score in the scored (0-100):"))   
if 0 <= marks_scored <=100:
 if marks_scored >= 90:
     grade = "A" 
 elif marks_scored >= 80:
     grade = "B"  
 elif marks_scored >= 70:
     grade = "C" 
 elif marks_scored >= 60:
     grade ="D"
 elif marks_scored >= 50:
     grade = "E"
 elif marks_scored <50:
     grade = "Fail"
     print("Grade",grade) 
else:
    print("Enter a value between 0 and 100.")
    
#Witi Academy is proposing a Sacco to help students save their money.
# Design a platform that willdo the following.
#  Deposite money 
# Withdrawl money 
# 3. Check Balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student select 2, money should be withdrawn and a minimum withdraw is 500.
# If the student selects 3, the account balance should be displayed
    balance =  0
    print("Welcome to WITU Academy Sacco")
    print("\nPlease choose an option")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check balance")
    
    choice = input("Enter your choice (1/2/3):")
    if choice == '1':
        amount = float(input("Enter amount to deposite: "))
        if amount >= 1000:
            balance += amount
            print(f"Successfully deposited {amount}. New balance is {balance}.")
        else:
            print("Minimum deposite amount is 1000.") 
    elif choice =='2':
        amount = float (input("Enter amount to withdraw:"))
        if amount  >= 500: 
            if balance >= amount:
                balance -= amount
                print(f"Successfully withdraw {amount}. New balance is {balance}.") 
            else:
                print("Insufficient balance.") 
        else:
            print("Minimum withdrawl amount is 500.")
    elif choice == '3':      #Check Balance
        print(f"Your current balance is {balance}.") 
    else:
        print("Invalid choice.")                       


