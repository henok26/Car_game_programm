command=""
started=False

while True:
    command=input(">").lower()
    if command=="start" :
        if started:
            print("car is already started")
        else:
            started=True
            print("started.......")


    elif command=="stop":
     if not started:
        print("car is already stopped")
     else:
      started=True
     print("car stoped")

    elif command=="help":
        print('''  press help for help
  press start to start 
  press quit to stop the game ''')
    elif command=="quit":
        break
    else:
        print("sorry i don't understand it")


