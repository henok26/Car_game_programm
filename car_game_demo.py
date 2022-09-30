started=False
command=""
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("car already started")
        else:
            started=True
        print("car starts")
    elif command == "quit":

            break
else:
                print("incorrect command")