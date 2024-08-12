import pyttsx3

print("It's Robo 1.1 Version...")
while(True):
    x=input("Enter what you want to speak (for Quit type q)): ")
    if x == "q":
        print("Ending...")
        break

    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
