print("")
print("")
print("                         🐍💧🔫 Welcome To The Snake Water Gun Game 🎮")
print("=*"*48)
print("                                                - : Game Rules : - ")
print("_"*153)
print("| We have three options: "," "*126,"|","\n|1. Snake 🐍"," "*139,"|"," \n|2. Water 💧"," "*139,"|","\n|3. Gun 🔫"," "*141,"|","\n| You should choose one, and I will choose one as well. We will then compare our choices and decide the round winner according to the following rules:   |")
print("|1. Snake 🐍 vs. Water 💧: Snake wins because it drinks the water."," "*85,"|","")
print("|2. Snake 🐍 vs. Gun 🔫: Gun wins because it shoots the snake."," "*89,"|","")
print("|3. Gun 🔫 vs. Water 💧: Water wins because the gun doesn't work properly in water."," "*68,"|","")
print("| The final winner is decided after 10 rounds based on the maximum number of round wins."," "*63,"|","")
print("|","_"*150,"|")
print("                                            LET'S START THE GAME 🎉")

import random
l = ['GUN','SNAKE','WATER']
mp = 0
yp = 0

for i in range(1,11):
    print("\n🎯 ROUND", i, "🎯")
    print("Choose any one option: 1. Snake 🐍  2. Water 💧  3. Gun 🔫")
    your = input("Your choice: ").lower()
    my = random.choice(l)
    print("🕹️ So, all done!")
    if your in ['g', 'gun', '3', '3.','GUN', 'Gun','G']:
        print("You chose: GUN 🔫")
        print("My pick was:", my)
        print("GUN 🔫 vs.", my)
        if my == 'GUN':
            print("🤝 It's a tie!")
        elif my == 'WATER':
            print("💧 Water wins! I win this round.")
            mp += 1
        else:
            print("🐍 Snake wins! You win this round.")
            yp += 1
    elif your in ['w', 'water', '2', '2.', 'WATER', 'Water', 'W']:
        print("You chose: WATER 💧")
        print("My pick was:", my)
        print("WATER 💧 vs.", my)
        if my == 'WATER':
            print("🤝 It's a tie!")
        elif my == 'SNAKE':
            print("🐍 Snake wins! I win this round.")
            mp += 1
        else:
            print("💧 Water wins! You win this round.")
            yp += 1
    elif your in ['s', 'snake', '1', '1.', 'SNAKE', 'Snake', 'S']:
        print("You chose: SNAKE 🐍")
        print("My pick was:", my)
        print("SNAKE 🐍 vs.", my)
        if my == 'SNAKE':
            print("🤝 It's a tie!")
        elif my == 'GUN':
            print("🔫 Gun wins! I win this round.")
            mp += 1
        else:
            print("🐍 Snake wins! You win this round.")
            yp += 1
    else:
        print("❌ Invalid input. Please choose 'Snake', 'Water', or 'Gun'.")
    print("📊 Score => You:", yp, "| Me:", mp)
    print("\n" + "="*130)

print("\n🏁 --: FINAL RESULT :-- 🏁")
if mp > yp:
    print("😞 Good try, but you lost this time.")
    print("🏆 The winner is Anshuman Singh! 👑")
elif yp > mp:
    print("🎉 Congratulations! You win the match! 🏆")
else:
    print("🤝 It's a tie! Let's play again to find the winner.")
