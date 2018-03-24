import random
arieltotal = 0
seertotal = 0
while (int(arieltotal) < 30) and (int(seertotal) < 30):
    yourturn = str(input("Press Enter to roll, or X to skip your turn.")).upper()
    if yourturn != "X":
        roll = random.randint(1, 6)
        arieltotal += roll
        print("You rolled a " + str(roll) + ".")
        if (roll == 1) and (arieltotal == 1):
            print("Your score is still 0!")
        elif (roll == 1) and (arieltotal != 1):
            arieltotal = 0
            print("Your score went back to 0!")
        else:
            print("Your total score is " + str(arieltotal) + ".")
            if (arieltotal >= 30):
                print("You won!")
        if (arieltotal < 30):
            herturn = str(input("Now wait for your opponent to roll. Press Enter."))
            seerschoice = random.randint(1,6)
            if (seerschoice < 3):
                print("Your opponent skipped their turn. It's your turn now!")
            else:
                herroll = random.randint(1, 6)
                seertotal += herroll
                print("Your opponent rolled a " + str(herroll) + ".")
                if (herroll == 1) and (seertotal != 1):
                    seertotal = 0
                    print("Their score went back to 0!")
                elif (herroll ==1) and (seertotal == 1):
                    print("Their score is still 0!")
                else:
                    print("Their total score is " + str(seertotal) + ".")
                    if (seertotal >= 30):
                        print("You lost!")
    else:
        herturn = str(input("Now wait for your opponent to roll. Press Enter."))
        seerschoice = random.randint(1,6)
        if (seerschoice < 3):
            print("Your opponent skipped their turn. It's your turn now!")
        else:
            herroll = random.randint(1, 6)
            seertotal += herroll
            print("Your opponent rolled a " + str(herroll) + ".")
            if (herroll == 1) and (seertotal != 0):
                seertotal = 0
                print("Their score went back to 0!")
            elif (herroll ==1) and (seertotal == 0):
                    print("Their score is still 0!")
            else:
                print("Their total score is " + str(seertotal) + ".")
                if (seertotal >= 30):
                    print("You lost!")
