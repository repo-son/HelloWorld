command = ""
is_start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if is_start:
            print("What!!! Car Already Started")
        else:
            is_start = True
            print("Car Started...")
    elif command == "stop":
        if not is_start:
            print("My God..It's Already Stopped")
        else:
            is_start = False
            print("Car Stopped...")
    elif command == "help":
        print("""
    start - to start the Car
    stop - Stop the Car
    quit - to Exit the Game
        """)
    elif command == "quit":
        print("See You")
        break
    else:
        print("I Really Don't Understand that, Sorry")