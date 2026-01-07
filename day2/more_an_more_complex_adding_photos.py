print("welcome to rollercoster")
bill=0
height=int(input("whta is your height in cm?"))
if height>120:
    print("you can ride")
    age=int(input("what is your age?"))
    if age<12:
        print("pay 5 rupee")
        bill=5
  
    elif age<18:
        print("pay 7 rupee")
        bill=7
    else:
        print("pay 12 rupee")
        bill=12
        photos=input("do you want pictures during rides?")
        if photos=="yes":   
            bill+=3
            print("the total bill is",bill)
else:
    print("you can't ride")
    
