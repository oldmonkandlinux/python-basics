'''
A simple game which asks for input (start,stop,help,quit) and based on inputs displays a message
start - starts the car
stop - stops the car
quit - quits the program
help - displays help
'''

command = ""
started = False
stopped = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car is started")

    elif command == "stop":
        if stopped:
            print("car is already stopped")
        else:
            stopped = True
            print("car is stopped")
    elif command == "help":
        print("""
        start - starts the car
        stop  - stops the car
        quit  - quits the program
        """)
    elif command == "quit":
        break
    else:
        print("sorry, i didn't understand that")