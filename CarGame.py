command = ""
Started = False
while True:
    command = input("> ").lower()
    if command == 'start' :
        if Started:
            print("car is already started!!")
        else:
            Started = True
            print("Car Started")
    elif command == 'stop':
        if not Started:
            print("car is already stopped!!")
        else:
            Started = False
            print("Car Stopped")
    elif command == 'quit':
        break
    elif command == 'help':
        print('''
        start  - to start the car
        stop   - to stop the car
        quit   - to quit the game
        ''')
    else:
        print("sorry,I dont't understand")