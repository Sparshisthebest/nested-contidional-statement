#your customised ride
print("select your ride")
print("1. bike")
print("2. car")
choice=int(input("enter your choice: "))
if(choice==1):
    print("what type of bike")
    print("1. scooty\n")
    print("2. scooter\n")
    choice2=int(input("enter your choice2: "))
    if(choice2==1):
        print("you have selected scootie")
    else:
        print("you have selected scooter")
elif(choice==2):
    print("what type of car do you want ?")
    print("1. tesla")
    print("2. rolls royce")
    choice3=int(input("enter your choice3: "))
    if choice3==1:
        print("you have selected tesla")
    else:
        print("you have selected rolls royce")
else:
    print("wrong choice!")
    
  
    
    
