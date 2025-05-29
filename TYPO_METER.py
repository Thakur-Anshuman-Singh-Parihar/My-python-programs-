from time import *
import random as rd
def speed():
    deff = etime - stime
    reald = round(deff,2)
    speed = len(uinput)/reald
    s = round(speed,2)
    print("totel time taken by you :-  ",reald)
    return s
def space():
    word = 0
    for i in range(len(uinput)):
        if (uinput[i] == uinput[i].isalpha()) and (uinput[i+1] == ' '):
            word = word + 1
    return word
def error():
    error = 0
    for i in range(len(uinput)):
        try :
            if uinput[i] != paragraph[i]:
                error = error + 1
        except:
            error = error + 1
    return error

while True :
    op = input('''enter "  1  " if you are ready for typing \n enter "  0  " for exit ...''' )
    if op == '1':
        print("start typing the timer was start....")
        parlist = ["The Indian social system is deeply rooted in its historical, cultural, and religious traditions. "
        "It is shaped by a unique set of values that influence individual behavior, societal norms, and governance."
        " These values promote harmony, diversity, and collective well-being.","The Indian social system prioritizes "
        "group interests overindividualism.Festivals, rituals, and social gatherings foster a sense of belonging"
        ".Rural communities often practice cooperative living and resource-sharing.",
        "Love for the nation and respect for national symbols (e.g., national anthem, tricolor flag)."
        "Participation in democratic processes like voting and civic duties.Sacrifices made by freedom fighters "
        "inspire modern youth.",
        "The values of the Indian social system have played a crucial role in maintaining harmony and stability"
        " in society. As responsible citizens, it is essential to uphold these values in daily life."
        ]
        paragraph = rd.choice(parlist)
        print("\n\n",paragraph,"\n\n")

        stime = time()
        uinput = input (" enter the paragraph :-   ")
        etime = time()
        print("your speed was : -  ",speed(),"charecter/second")
        print("totel character you typed :-  ",len(uinput))
        print("totel error goted is :- ",error())
        print(space())
    elif op == '0':
        print("thank you for visiting......")
        break
    else:
        print("Invalid Input")
