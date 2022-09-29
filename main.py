command=""
while True:
    command=input(">").lower()
    if command=="start" :
        print("started.......")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print('''  press help for help
  press start to start 
  press quit to stop the game ''')
    elif command=="quit":
        break
    else:
        print("sorry i don't understand it")


