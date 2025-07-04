import time
import random
import turtle
wn=turtle.Screen()
wn.bgcolor("black")
while True:
    print()
    print()
    t=turtle.Turtle()
    m=turtle.Turtle()
    m.clear()
    m.clear()
    t.clear()
    t.clear()
    m.ht()
    t.color("green")
    t.write("Welcome to Our Game! \n 1.TicTacToe \n 2.Hangman \n 3.Exit",move=False,align="center",font=("Calibri",30,"normal"))
    t.ht()
    print("Welcome to Our Game!")
    print("1.TicTacToe")
    print("2.Hangman")
    print("3.Exit")
    Enter=input("Enter your choice: ")
    if Enter=="3":
        m.clear()
        t.clear()
        t.color("green")
        print()
        print()
        t.write("________________________Credits________________________",move=False,align="center",font=("Calibri",20,"normal"))
        print("________________________Credits________________________")
        time.sleep(1)
        t.clear()
        t.write("________________________Credits________________________ \n ------------------------Creators------------------------ \n Sreyas \n Dharshan \n Stupid Bot \n World Class Player ",move=False,align="center",font=("Calibri",20,"normal"))
        print("------------------------Creators------------------------")
        print("Sreyas")
        print("Dharshan")
        print("Stupid Bot")
        print("World Class Player")
        time.sleep(1)
        t.clear()
        print()
        print()
        t.write("________________________Credits________________________ \n ------------------------Creators------------------------ \n Sreyas \n Dharshan \n Stupid Bot \n World Class Player \n -------------------------------------------------------- \n ________________________Bye:)__________________________",move=False,align="center",font=("Calibri",20,"normal"))
        print("--------------------------------------------------------")
        print("________________________Bye:)__________________________")
        time.sleep(5)
        break
    elif Enter=="1":
        m.clear()
        while True:
            X1,X2,X3,X4,X5,X6,X7,X8,X9="7 ","8 ","9 ","4 ","5 ","6 ","1 ","2 ","3 "
            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
            print("                +                +         ")
            print("                +                +         ")
            print("----------------+----------------+---------------")
            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
            print("                +                +        ")
            print("                +                +        ")
            print("----------------+----------------+---------------")
            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
            print("                +                +        ")
            print("                +                +        ")
            print()
            print()
            t.clear()
            t.color("blue")
            t.ht()
            t.write("Welcome to a new game of TicTacToe!",move=False,align="center",font=("Calibri",30,"normal"))
            time.sleep(2)
            t.clear()
            t.write("1.SinglePlayer \n 2.Multiplayer \n 3.Back",move=False,align="center",font=("Calibri",30,"normal"))
            print("Welcome to TicTacToe!")
            print("1.SinglePlayer")
            print("2.Multiplayer")
            print("3.Back")
            x=input("Enter your choice: ")
            if x=="3":
                t.clear()
                break
            elif x=="1":
                t.clear()
                print()
                print()
                t.write("Choose your difficulty: \n 1.EZ (against a stupid bot) \n 2.WORLD-CLASS ",move=False,align="center",font=("Calibri",30,"normal"))
                print("Choose your difficulty:")
                print("1.EZ (against a stupid bot)")
                print("2.WORLD-CLASS ")
                dif=input("Enter: ")
                if dif=="1":
                    t.clear()
                    t.write("        7       +        8     +        9 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        4       +        5     +        6 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        1       +        2     +        3 \n",move=False,align="center",font=("Calibri",15,"normal"))
                    List=[X1,X2,X3,X4,X5,X6,X7,X8,X9]
                    number="123456789"
                    Turns1=5
                    Turns2=4
                    P1choice=""
                    P2choice=""
                    while Turns1>=0 and Turns2>=0:
                        if Turns1==5:
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                        else:
                            if X1[0]!="X" and X1[0]!="O":
                                X1="  "
                            if X2[0]!="X" and X2[0]!="O":
                                X2="  "
                            if X3[0]!="X" and X3[0]!="O":
                                X3="  "
                            if X4[0]!="X" and X4[0]!="O":
                                X4="  "
                            if X5[0]!="X" and X5[0]!="O":
                                X5="  "
                            if X6[0]!="X" and X6[0]!="O":
                                X6="  "
                            if X7[0]!="X" and X7[0]!="O":
                                X7="  "
                            if X8[0]!="X" and X8[0]!="O":
                                X8="  "
                            if X9[0]!="X" and X9[0]!="O":
                                X9="  "
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                        if Turns1>Turns2:
                            print("It's your chance:")
                            print()
                            p1=str(input("Enter Position(9-1): "))
                            if len(p1)==1 and p1 in number and p1 not in P2choice and p1 not in P1choice:
                                P1choice+=p1
                                Turns1-=1
                        else:
                            print("It's the Stupid Bot chance:")
                            print()
                            p2=str(random.randint(1,10))
                            while (p2 not in P2choice and p2 in number and p2  in P1choice) or (p2 in P2choice and p2 in number and p2  not in P1choice):
                                p2=str(random.randint(1,10))
                            else:
                                P2choice+=p2
                                Turns2-=1
                                
                        
                        for i in number:
                            if i in P1choice:
                                if i=="7":
                                    X1="X "
                                if i=="8":
                                    X2="X "
                                if i=="9":
                                    X3="X "
                                if i=="4":
                                    X4="X "
                                if i=="5":
                                    X5="X "
                                if i=="6":
                                    X6="X "
                                if i=="1":
                                    X7="X "
                                if i=="2":
                                    X8="X "
                                if i=="3":
                                    X9="X "
                            if i in P1choice:
                                if i=="7":
                                    X1="O "
                                if i=="8":
                                    X2="O "
                                if i=="9":
                                    X3="O "
                                if i=="6":
                                    X4="O "
                                if i=="5":
                                    X5="O "
                                if i=="4":
                                    X6="O "
                                if i=="1":
                                    X7="O "
                                if i=="2":
                                    X8="O "
                                if i=="3":
                                    X9="O "
                
                        for i in number:
                            if i in P1choice:
                                if i=="7":
                                    X1="X "
                                if i=="8":
                                    X2="X "
                                if i=="9":
                                    X3="X "
                                if i=="4":
                                    X4="X "
                                if i=="5":
                                    X5="X "
                                if i=="6":
                                    X6="X "
                                if i=="1":
                                    X7="X "
                                if i=="2":
                                    X8="X "
                                if i=="3":
                                    X9="X "
                            if i in P2choice:
                                if i=="7":
                                    X1="O "
                                if i=="8":
                                    X2="O "
                                if i=="9":
                                    X3="O "
                                if i=="4":
                                    X4="O "
                                if i=="5":
                                    X5="O "
                                if i=="6":
                                    X6="O "
                                if i=="1":
                                    X7="O "
                                if i=="2":
                                    X8="O "
                                if i=="3":
                                    X9="O "
                                
                        if (X1=="X " and X2=="X " and X3=="X ") or (X1=="X " and X4=="X " and X7=="X ") or (X2=="X " and X5=="X " and X8=="X ") or (X3=="X " and X6=="X " and X9=="X ") or (X3=="X " and X5=="X " and X7=="X ") or (X4=="X " and X5=="X " and X6=="X ") or (X7=="X " and X8=="X " and X9=="X ") or (X1=="X " and X5=="X " and X9=="X "):
                            print("You Win!")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break
                        if (X1=="O " and X2=="O " and X3=="O ") or (X1=="O " and X4=="O " and X7=="O ") or (X2=="O " and X5=="O " and X8=="O ") or (X3=="O " and X6=="O " and X9=="O ") or (X3=="O " and X5=="O " and X7=="O ") or (X4=="O " and X5=="O " and X6=="O ") or (X7=="O " and X8=="O " and X9=="O ") or (X1=="O " and X5=="O " and X9=="O "):
                            print("Stupid Bot Wins! You SUCK !")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break
                        if Turns1==0 and Turns2==0 and (X1!="  " and X2!="  " and X3!="  " and X4!="  " and X5!="  " and X6!="  " and X7!="  " and X8!="  " and X9!="  "):
                            print("Its a draw!")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break
                elif dif=="2":
                    t.clear()
                    t.write("        7       +        8     +        9 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        4       +        5     +        6 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        1       +        2     +        3 \n",move=False,align="center",font=("Calibri",15,"normal"))
                    List=[X1,X2,X3,X4,X5,X6,X7,X8,X9]
                    number="123456789"
                    Turns1=5
                    Turns2=4
                    P1choice=""
                    P2choice=""
                    corner="7913"
                    edge="2468"
                    center="5"
                    while Turns1>=0 and Turns2>=0:
                        if Turns1==5:
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                        else:
                            if X1[0]!="X" and X1[0]!="O":
                                X1="  "
                            if X2[0]!="X" and X2[0]!="O":
                                X2="  "
                            if X3[0]!="X" and X3[0]!="O":
                                X3="  "
                            if X4[0]!="X" and X4[0]!="O":
                                X4="  "
                            if X5[0]!="X" and X5[0]!="O":
                                X5="  "
                            if X6[0]!="X" and X6[0]!="O":
                                X6="  "
                            if X7[0]!="X" and X7[0]!="O":
                                X7="  "
                            if X8[0]!="X" and X8[0]!="O":
                                X8="  "
                            if X9[0]!="X" and X9[0]!="O":
                                X9="  "
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                        if Turns1>Turns2:
                            print("It's the World Class Player's chance:")
                            print()
                            if Turns1==5:
                                p1=random.choice(corner)
                                p1=str(p1)
                                P1choice+=p1
                                Turns1-=1
                            elif Turns1==4:
                                for i in P2choice:
                                    if i in center:
                                        p1=10-int(P1choice[0])
                                        p1=str(p1)
                                        P1choice+=p1
                                        
                                    elif i in edge:
                                        if P1choice=="7":
                                            if P2choice=="8" or P2choice=="2":
                                                p1="1"
                                            elif P2choice=="4" or P2choice=="6":
                                                p1="9"
                                            P1choice+=p1
                                            
                                        elif P1choice=="1":
                                            if P2choice=="8" or P2choice=="2":
                                                p1="7"
                                            elif P2choice=="4" or P2choice=="6":
                                                p1="3"
                                            P1choice+=p1
                                            
                                        elif P1choice=="3":
                                            if P2choice=="8" or P2choice=="2":
                                                p1="9"
                                            elif P2choice=="4" or P2choice=="6":
                                                p1="1"
                                            P1choice+=p1
                                            
                                        elif P1choice=="9":
                                            if P2choice=="8" or P2choice=="2":
                                                p1="3"
                                            elif P2choice=="4" or P2choice=="6":
                                                p1="7"
                                            P1choice+=p1
                                            
                                    elif i in corner:
                                        p1=10-int(P1choice[0])
                                        if P2choice==str(p1):
                                            if P2choice=="3" or P2choice=="7":
                                                p1="1"
                                            elif P2choice=="1" or P2choice=="9":
                                                p1="3"
                                            P1choice+=p1
                                            
                                        else:
                                            if P1choice=="7":
                                                if P2choice=="1":
                                                    p1="8"
                                                elif P2choice=="9":
                                                    p1="4"
                                                P1choice+=p1
                                            elif P1choice=="1":
                                                if P2choice=="7":
                                                    p1="2"
                                                elif P2choice=="3":
                                                    p1="4"
                                                P1choice+=p1
                                            elif P1choice=="3":
                                                if P2choice=="9":
                                                    p1="2"
                                                elif P2choice=="1":
                                                    p1="6"
                                                P1choice+=p1
                                            elif P1choice=="9":
                                                if P2choice=="3":
                                                    p1="8"
                                                elif P2choice=="7" :
                                                    p1="6"
                                                    P1choice+=p1
                                else:
                                    Turns1-=1
                            elif Turns1==3:
                                if "3" in P1choice and "2" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "2" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "1" in P1choice and "4" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "7" in P1choice and "4" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "7" in P1choice and "8" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "8" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "9" in P1choice and "6" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "3" in P1choice and "6" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "1" in P1choice and "3" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "1" in P1choice and "7" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "7" in P1choice and "9" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "9" in P1choice and "3" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "1" in P1choice and "5" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "5" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "9" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "3" in P1choice and "5" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "5" in P1choice and "7" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "7" in P1choice and "3" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "2" in P1choice and "5" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "2" in P1choice and "8" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "5" in P1choice and "8" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "4" in P1choice and "5" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "6" in P1choice and "5" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "6" in P1choice and "4" in P1choice and "5" not in P2choice:
                                    p1="5"
                                
                                
                                #comment
                                elif "3" in P2choice and "2" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "2" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "1" in P2choice and "4" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "7" in P2choice and "4" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "7" in P2choice and "8" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "8" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "9" in P2choice and "6" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "3" in P2choice and "6" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "1" in P2choice and "3" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "1" in P2choice and "7" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "7" in P2choice and "9" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "9" in P2choice and "3" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "1" in P2choice and "5" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "5" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "9" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "3" in P2choice and "5" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "5" in P2choice and "7" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "7" in P2choice and "3" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "2" in P2choice and "5" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "2" in P2choice and "8" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "5" in P2choice and "8" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "4" in P2choice and "5" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "6" in P2choice and "5" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "6" in P2choice and "4" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "5" in P2choice:
                                    if "2" not in P2choice and "6" not in P2choice and "8" not in P2choice and "4" not in P2choice:
                                        p1=P2choice[-1]
                                        p1=int(p1)
                                        p1=10-p1
                                elif P2choice[-1] in edge and P2choice[0] in edge:
                                    p1="5"
                                elif P2choice[-1] in corner and P2choice[0] in corner:
                                    p1="5"
                                elif P2choice[-1] in edge and P2choice[0] in corner:
                                    while (p1 not in P2choice and p1 in number and p1  in P1choice) or (p1 in P2choice and p1 in number and p1  not in P1choice):
                                        p1=random.choice(corner)                                 
                                P1choice+=p1
                                Turns1-=1
                            elif Turns1==2:
                                if "3" in P1choice and "2" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "2" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "1" in P1choice and "4" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "7" in P1choice and "4" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "7" in P1choice and "8" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "8" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "9" in P1choice and "6" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "3" in P1choice and "6" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "1" in P1choice and "3" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "1" in P1choice and "7" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "7" in P1choice and "9" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "9" in P1choice and "3" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "1" in P1choice and "5" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "5" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "9" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "3" in P1choice and "5" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "5" in P1choice and "7" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "7" in P1choice and "3" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "2" in P1choice and "5" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "2" in P1choice and "8" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "5" in P1choice and "8" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "4" in P1choice and "5" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "6" in P1choice and "5" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "6" in P1choice and "4" in P1choice and "5" not in P2choice:
                                    p1="5"
                                
                                
                                #comment
                                elif "3" in P2choice and "2" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "2" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "1" in P2choice and "4" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "7" in P2choice and "4" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "7" in P2choice and "8" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "8" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "9" in P2choice and "6" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "3" in P2choice and "6" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "1" in P2choice and "3" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "1" in P2choice and "7" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "7" in P2choice and "9" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "9" in P2choice and "3" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "1" in P2choice and "5" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "5" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "9" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "3" in P2choice and "5" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "5" in P2choice and "7" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "7" in P2choice and "3" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "2" in P2choice and "5" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "2" in P2choice and "8" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "5" in P2choice and "8" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "4" in P2choice and "5" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "6" in P2choice and "5" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "6" in P2choice and "4" in P2choice and "5" not in P1choice:
                                    p1="5"
                                else:
                                    p1=str(random.randint(1,10))
                                    while (p1 not in P1choice and p1 in number and p1  in P1choice) or (p1 in P2choice and p1 in number and p1  not in P1choice):
                                        p1=str(random.randint(1,10))
                                    else:
                                        P2choice+=p2
                                        Turns1-=1
                                P1choice+=p1
                                Turns1-=1    
                            elif Turns1==1:
                                if "3" in P1choice and "2" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "2" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "1" in P1choice and "4" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "7" in P1choice and "4" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "7" in P1choice and "8" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "8" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "9" in P1choice and "6" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "3" in P1choice and "6" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "1" in P1choice and "3" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "1" in P1choice and "7" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "7" in P1choice and "9" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "9" in P1choice and "3" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "1" in P1choice and "5" in P1choice and "9" not in P2choice:
                                    p1="9"
                                elif "9" in P1choice and "5" in P1choice and "1" not in P2choice:
                                    p1="1"
                                elif "1" in P1choice and "9" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "3" in P1choice and "5" in P1choice and "7" not in P2choice:
                                    p1="7"
                                elif "5" in P1choice and "7" in P1choice and "3" not in P2choice:
                                    p1="3"
                                elif "7" in P1choice and "3" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "2" in P1choice and "5" in P1choice and "8" not in P2choice:
                                    p1="8"
                                elif "2" in P1choice and "8" in P1choice and "5" not in P2choice:
                                    p1="5"
                                elif "5" in P1choice and "8" in P1choice and "2" not in P2choice:
                                    p1="2"
                                elif "4" in P1choice and "5" in P1choice and "6" not in P2choice:
                                    p1="6"
                                elif "6" in P1choice and "5" in P1choice and "4" not in P2choice:
                                    p1="4"
                                elif "6" in P1choice and "4" in P1choice and "5" not in P2choice:
                                    p1="5"
                                
                                
                                #comment
                                elif "3" in P2choice and "2" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "2" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "1" in P2choice and "4" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "7" in P2choice and "4" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "7" in P2choice and "8" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "8" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "9" in P2choice and "6" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "3" in P2choice and "6" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "1" in P2choice and "3" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "1" in P2choice and "7" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "7" in P2choice and "9" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "9" in P2choice and "3" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "1" in P2choice and "5" in P2choice and "9" not in P1choice:
                                    p1="9"
                                elif "9" in P2choice and "5" in P2choice and "1" not in P1choice:
                                    p1="1"
                                elif "1" in P2choice and "9" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "3" in P2choice and "5" in P2choice and "7" not in P1choice:
                                    p1="7"
                                elif "5" in P2choice and "7" in P2choice and "3" not in P1choice:
                                    p1="3"
                                elif "7" in P2choice and "3" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "2" in P2choice and "5" in P2choice and "8" not in P1choice:
                                    p1="8"
                                elif "2" in P2choice and "8" in P2choice and "5" not in P1choice:
                                    p1="5"
                                elif "5" in P2choice and "8" in P2choice and "2" not in P1choice:
                                    p1="2"
                                elif "4" in P2choice and "5" in P2choice and "6" not in P1choice:
                                    p1="6"
                                elif "6" in P2choice and "5" in P2choice and "4" not in P1choice:
                                    p1="4"
                                elif "6" in P2choice and "4" in P2choice and "5" not in P1choice:
                                    p1="5"
                                else:
                                    p1=str(random.randint(1,10))
                                    while (p1 not in P1choice and p1 in number and p1  in P1choice) or (p1 in P2choice and p1 in number and p1  not in P1choice):
                                        p1=str(random.randint(1,10))
                                    else:
                                        P2choice+=p2
                                        Turns1-=1
                                P1choice+=p1
                                Turns1-=1
                        else:
                            print("It's your chance:")
                            print()
                            p2=str(input("Enter Position(9-1): "))
                            if len(p2)==1 and p2 in number and p2 not in P2choice and p2 not in P1choice:
                                P2choice+=p2
                                Turns2-=1
                        for i in number:
                            if i in P1choice:
                                if i=="7":
                                    X1="X "
                                if i=="8":
                                    X2="X "
                                if i=="9":
                                    X3="X "
                                if i=="4":
                                    X4="X "
                                if i=="5":
                                    X5="X "
                                if i=="6":
                                    X6="X "
                                if i=="1":
                                    X7="X "
                                if i=="2":
                                    X8="X "
                                if i=="3":
                                    X9="X "
                            if i in P1choice:
                                if i=="7":
                                    X1="O "
                                if i=="8":
                                    X2="O "
                                if i=="9":
                                    X3="O "
                                if i=="4":
                                    X4="O "
                                if i=="5":
                                    X5="O "
                                if i=="6":
                                    X6="O "
                                if i=="1":
                                    X7="O "
                                if i=="2":
                                    X8="O "
                                if i=="3":
                                    X9="O "
                
                        for i in number:
                            if i in P1choice:
                                if i=="7":
                                    X1="X "
                                if i=="8":
                                    X2="X "
                                if i=="9":
                                    X3="X "
                                if i=="4":
                                    X4="X "
                                if i=="5":
                                    X5="X "
                                if i=="6":
                                    X6="X "
                                if i=="1":
                                    X7="X "
                                if i=="2":
                                    X8="X "
                                if i=="3":
                                    X9="X "
                            if i in P2choice:
                                if i=="7":
                                    X1="O "
                                if i=="8":
                                    X2="O "
                                if i=="9":
                                    X3="O "
                                if i=="4":
                                    X4="O "
                                if i=="5":
                                    X5="O "
                                if i=="6":
                                    X6="O "
                                if i=="1":
                                    X7="O "
                                if i=="2":
                                    X8="O "
                                if i=="3":
                                    X9="O "
                            
                        if (X1=="X " and X2=="X " and X3=="X ") or (X1=="X " and X4=="X " and X7=="X ") or (X2=="X " and X5=="X " and X8=="X ") or (X3=="X " and X6=="X " and X9=="X ") or (X3=="X " and X5=="X " and X7=="X ") or (X4=="X " and X5=="X " and X6=="X ") or (X7=="X " and X8=="X " and X9=="X ") or (X1=="X " and X5=="X " and X9=="X "):
                            print("World Class Player wins! and its not You.")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break
                        if (X1=="O " and X2=="O " and X3=="O ") or (X1=="O " and X4=="O " and X7=="O ") or (X2=="O " and X5=="O " and X8=="O ") or (X3=="O " and X6=="O " and X9=="O ") or (X3=="O " and X5=="O " and X7=="O ") or (X4=="O " and X5=="O " and X6=="O ") or (X7=="O " and X8=="O " and X9=="O ") or (X1=="O " and X5=="O " and X9=="O "):
                            print("You Win! What sorcery is this?!")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break
                        if Turns1==0 and Turns2==0 and (X1!="  " and X2!="  " and X3!="  " and X4!="  " and X5!="  " and X6!="  " and X7!="  " and X8!="  " and X9!="  "):
                            print("Its a draw!")
                            print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                            print("                +                +         ")
                            print("                +                +         ")
                            print("----------------+----------------+---------------")
                            print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print("----------------+----------------+---------------")
                            print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                            print("                +                +        ")
                            print("                +                +        ")
                            print()
                            print()
                            print()
                            print()
                            print()
                            break




                        continue
            elif x=="2":
                m.clear()
                t.clear()
                t.write("        7       +        8     +        9 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        4       +        5     +        6 \n                 +               +          \n                 +               +          \n  ________+_______+_______ \n        1       +        2     +        3 \n",move=False,align="center",font=("Calibri",15,"normal"))
                List=[X1,X2,X3,X4,X5,X6,X7,X8,X9]
                number="123456789"
                Turns1=5
                Turns2=4
                P1choice=""
                P2choice=""
                Player1=str(input("Enter Player1's name (X)"))
                Player2=str(input("Enter Player2's name (O)"))
                while Turns1>=0 and Turns2>=0:
                    if Turns1==5:
                        print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                        print("                +                +         ")
                        print("                +                +         ")
                        print("----------------+----------------+---------------")
                        print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print("----------------+----------------+---------------")
                        print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                    else:
                        if X1[0]!="X" and X1[0]!="O":
                            X1="  "
                        if X2[0]!="X" and X2[0]!="O":
                            X2="  "
                        if X3[0]!="X" and X3[0]!="O":
                            X3="  "
                        if X4[0]!="X" and X4[0]!="O":
                            X4="  "
                        if X5[0]!="X" and X5[0]!="O":
                            X5="  "
                        if X6[0]!="X" and X6[0]!="O":
                            X6="  "
                        if X7[0]!="X" and X7[0]!="O":
                            X7="  "
                        if X8[0]!="X" and X8[0]!="O":
                            X8="  "
                        if X9[0]!="X" and X9[0]!="O":
                            X9="  "
                        print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                        print("                +                +         ")
                        print("                +                +         ")
                        print("----------------+----------------+---------------")
                        print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print("----------------+----------------+---------------")
                        print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                    if Turns1>Turns2:
                        print("It's ",Player1,"'s chance: ")
                        print()
                        p1=str(input("Enter Position(9-1): "))
                        if len(p1)==1 and p1 in number and p1 not in P2choice and p1 not in P1choice:
                            P1choice+=p1
                            Turns1-=1
                    else:
                        print("It's ",Player2,"'s chance: ")
                        print()
                        p2=str(input("Enter Position(9-1): "))
                        if len(p2)==1 and p2 in number and p2 not in P2choice and p2 not in P1choice:
                            P2choice+=p2
                            Turns2-=1
                    for i in number:
                        if i in P1choice:
                            if i=="7":
                                X1="X "
                            if i=="8":
                                X2="X "
                            if i=="9":
                                X3="X "
                            if i=="4":
                                X4="X "
                            if i=="5":
                                X5="X "
                            if i=="6":
                                X6="X "
                            if i=="1":
                                X7="X "
                            if i=="2":
                                X8="X "
                            if i=="3":
                                X9="X "
                        if i in P2choice:
                            if i=="7":
                                X1="O "
                            if i=="8":
                                X2="O "
                            if i=="9":
                                X3="O "
                            if i=="4":
                                X4="O "
                            if i=="5":
                                X5="O "
                            if i=="6":
                                X6="O "
                            if i=="1":
                                X7="O "
                            if i=="2":
                                X8="O "
                            if i=="3":
                                X9="O "
                    if (X1=="X " and X2=="X " and X3=="X ") or (X1=="X " and X4=="X " and X7=="X ") or (X2=="X " and X5=="X " and X8=="X ") or (X3=="X " and X6=="X " and X9=="X ") or (X3=="X " and X5=="X " and X7=="X ") or (X4=="X " and X5=="X " and X6=="X ") or (X7=="X " and X8=="X " and X9=="X ") or (X1=="X " and X5=="X " and X9=="X "):
                        print(Player1," Wins!")
                        print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                        print("                +                +         ")
                        print("                +                +         ")
                        print("----------------+----------------+---------------")
                        print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print("----------------+----------------+---------------")
                        print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print()
                        print()
                        print()
                        print()
                        print()
                        break
                    if (X1=="O " and X2=="O " and X3=="O ") or (X1=="O " and X4=="O " and X7=="O ") or (X2=="O " and X5=="O " and X8=="O ") or (X3=="O " and X6=="O " and X9=="O ") or (X3=="O " and X5=="O " and X7=="O ") or (X4=="O " and X5=="O " and X6=="O ") or (X7=="O " and X8=="O " and X9=="O ") or (X1=="O " and X5=="O " and X9=="O "):
                        print(Player2," Wins!")
                        print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                        print("                +                +         ")
                        print("                +                +         ")
                        print("----------------+----------------+---------------")
                        print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print("----------------+----------------+---------------")
                        print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print()
                        print()
                        print()
                        print()
                        print()
                        break
                    if Turns1==0 and Turns2==0 and (X1!="  " and X2!="  " and X3!="  " and X4!="  " and X5!="  " and X6!="  " and X7!="  " and X8!="  " and X9!="  "):
                        print("Its a draw!")
                        print("        ",X1,"      +        ",X2,"      +        ",X3,sep="")
                        print("                +                +         ")
                        print("                +                +         ")
                        print("----------------+----------------+---------------")
                        print("        ",X4,"      +        ",X5,"      +        ",X6,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print("----------------+----------------+---------------")
                        print("        ",X7,"      +        ",X8,"      +        ",X9,sep="")
                        print("                +                +        ")
                        print("                +                +        ")
                        print()
                        print()
                        print()
                        print()
                        print()
                        break
    elif Enter=="2":
        m.clear()
        t.clear()
        print()
        print()
        while True:
            t=turtle.Turtle()
            m=turtle.Turtle()
            m.clear()
            m.color("white")
            m.ht()
            t.clear()
            t.color("blue")
            t.ht()
            t.write("Welcome to a new game of Hangman!",move=False,align="center",font=("Calibri",30,"normal"))
            time.sleep(3)
            t.clear()
            t.color("red")
            t.pu()
            t.setx(-250)
            t.sety(80)
            t.pd()
            t.speed(50)
            t.fd(100)
            t.rt(180)
            t.fd(50)
            t.rt(90)
            t.fd(170)
            t.rt(90)
            t.fd(100)
            t.rt(90)
            t.fd(50)
            t.pu()
            t.ht()
            print("Welcome to Hangman!")
            print()
            print("Choose a Category:")
            print("1.Movies")
            print("2.Celebrities/Famous People")
            print("3.Places")
            print("4.Exit")
            a=str(input("Enter Choice: "))
            if a=="4":
                t.clear()
                m.clear()
                break
            elif a=="1":
                LIST=["avengers endgame","avengers","joker","spiderman","spiderman 2","spiderman 3","the amazing spiderman","the amazing spiderman 2","spiderman homecoming","spiderman far from home","avengers infinity war","the godfather","deadpool","deadpool2","jumanji","jumanji welcome to the jungle",\
                      "detective pikachu","the dark knight rises", "streetlight","now you see me","now you see me"]
                word=random.randint(0,len(LIST)-1)
                word=LIST[word]
                hiddenword=""
                guess=""
                turns=6
                while turns>0:
                    hiddenword=""
                    fail=0
                    for i in word:
                        m.clear()
                        if i in guess:
                            print(i,end=" ")
                            hiddenword+=i
                            hiddenword+=" "
                        elif i==" ":
                            print(end="    ")
                            hiddenword+="    "  
                        elif i!=" ":
                            print("_",end=" ")
                            hiddenword+="_ "
                            fail+=1
                        t.pu()
                        m.pu()
                        m.sety(0)
                        m.setx(0)
                        m.color("white")
                        m.write(hiddenword,move=False,font=("Calibri",15,"normal"))
                    print()
                        

                    if fail==0:
                        print()
                        time.sleep(1)
                        print("You Won!")
                        t.clear()
                        m.clear()
                        t.color("blue")
                        t.write("You Won! :)",move=False,font=("Calibri",60,"normal"))
                        time.sleep(3)
                        t.clear()
                        m.clear()
                        break
                    print()
                    guesses=input("Guess a Letter ")
                    print()
                    print()
                    guesses=guesses.lower()
                    if len(guesses)==1:
                        guess+=guesses
                        if guesses not in word:
                            t.color("red")
                            turns-=1
                            print("Incorrect")
                            print("You have",turns,"more guesses")
                            print()
                            print()
                            print()
                            if turns==5:
                                t.pu()
                                t.setx(-120)
                                t.sety(180)
                                t.pd()
                                t.circle(20)
                                t.ht()
                            elif turns==4:
                                t.pu()
                                t.setx(-100)
                                t.sety(160)
                                t.pd()
                                t.fd(50)
                                t.ht()
                            elif turns==3:
                                t.rt(45)
                                t.fd(30)
                                t.ht()
                            elif turns==2:
                                t.pu()
                                t.rt(-90)
                                t.setx(-100)
                                t.sety(110)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==1:
                                t.pu()
                                t.rt(-45)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==0:
                                t.pu()
                                t.rt(180)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.pu()
                                t.ht()
                                time.sleep(1)
                                print("You Lost")
                                print("The movie was ",word)
                                t.clear()
                                m.clear()
                                t.color("red")
                                t.write("You Lost! :(",move=False,align="center",font=("Calibri",60,"normal"))
                                time.sleep(3)
                                t.clear()
                                m.clear()
                                break
            elif a=="2":
                LIST=["steve jobs","mahatma gandhi","robert downey jr","tom holland","narendra modi","rahul gandhi","chris pratt","dwyne johnson","keanu reeves","danny devito","hugh jackman","tom cruise","ryan reynolds","j k rowling","benedict cumberbatch","mark zuckerberg","bill gates","jeff bezos","sundar pichai","rajinikanth","jackiechan","kamal haasan","donald trump","abraham lincoln","charles babbage","alexander graham bell"]
                word=random.randint(0,len(LIST)-1)
                word=LIST[word]
                guess=""
                turns=6
                while turns>0:
                    hiddenword=""
                    fail=0
                    for i in word:
                        m.clear()
                        if i in guess:
                            print(i,end=" ")
                            hiddenword+=i
                            hiddenword+=" "
                        elif i==" ":
                            print(end="    ")
                            hiddenword+="    "  
                        elif i!=" ":
                            print("_",end=" ")
                            hiddenword+="_ "
                            fail+=1
                    
                        t.pu()
                        m.pu()
                        m.sety(0)
                        m.setx(0)
                        m.color("white")
                        m.write(hiddenword,move=False,font=("Calibri",15,"normal"))
                    if fail==0:
                        print()
                        time.sleep(1)
                        print("You Won")
                        t.clear()
                        m.clear()
                        t.color("blue")
                        t.write("You Won! :)",move=False,align="center",font=("Calibri",60,"normal"))
                        time.sleep(3)
                        t.clear()
                        m.clear()
                        break
                    print()
                    guesses=str(input("Guess a Letter "))
                    print()
                    guesses=guesses.lower()
                    if len(guesses)==1:
                        guess+=guesses
                        if guesses not in word:
                            turns-=1
                            print()
                            print()
                            print()
                            print("Incorrect")
                            print("You have",turns,"more guesses")
                            if turns==5:
                                t.pu()
                                t.setx(-120)
                                t.sety(180)
                                t.pd()
                                t.circle(20)
                                t.ht()
                            elif turns==4:
                                t.pu()
                                t.setx(-100)
                                t.sety(160)
                                t.pd()
                                t.fd(50)
                                t.ht()
                            elif turns==3:
                                t.rt(45)
                                t.fd(30)
                                t.ht()
                            elif turns==2:
                                t.pu()
                                t.rt(-90)
                                t.setx(-100)
                                t.sety(110)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==1:
                                t.pu()
                                t.rt(-45)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==0:
                                t.pu()
                                t.rt(180)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.pu()
                                t.ht()
                                time.sleep(1)
                                print("You Lost")
                                print("The person was ",word)
                                t.clear()
                                m.clear()
                                t.color("red")
                                t.write("You Lost! :(",move=False,align="center",font=("Calibri",60,"normal"))
                                time.sleep(3)
                                t.clear()
                                m.clear()
                                break
            elif a=="3":
                LIST=["london","chennai","banglore","kochi","new delhi","buenos aires","dubai","tokyo","beijing","capetown","florida","new york","washington dc","new jersey","san fransisco","munich","bern","paris","berlin","rome","canberra","melbourne"]
                word=random.randint(0,len(LIST)-1)
                word=LIST[word]
                guess=""
                turns=6
                while turns>0:
                    hiddenword=""
                    fail=0
                    for i in word:
                        m.clear()
                        if i in guess:
                            print(i,end=" ")
                            hiddenword+=i
                            hiddenword+=" "
                        elif i==" ":
                            print(end="    ")
                            hiddenword+="    "  
                        elif i!=" ":
                            print("_",end=" ")
                            hiddenword+="_ "
                            fail+=1
                        t.pu()
                        m.pu()
                        m.sety(0)
                        m.setx(0)
                        m.color("white")
                        m.write(hiddenword,move=False,font=("Calibri",15,"normal"))
                    if fail==0:
                        print()
                        time.sleep(1)
                        print("You Won")
                        t.clear()
                        m.clear()
                        t.color("blue")
                        t.write("You Won! :)",move=False,align="center",font=("Calibri",60,"normal"))
                        time.sleep(3)
                        m.clear()
                        t.clear()
                        break
                    print()
                    guesses=input("Guess a Letter ")
                    print()
                    guesses=guesses.lower()
                    if len(guesses)==1:
                        guess+=guesses
                        if guesses not in word:
                            turns-=1
                            print()
                            print()
                            print()
                            print("Incorrect")
                            print("You have",turns,"more guesses")
                            if turns==5:
                                t.pu()
                                t.setx(-120)
                                t.sety(180)
                                t.pd()
                                t.circle(20)
                                t.ht()
                            elif turns==4:
                                t.pu()
                                t.setx(-100)
                                t.sety(160)
                                t.pd()
                                t.fd(50)
                                t.ht()
                            elif turns==3:
                                t.rt(45)
                                t.fd(30)
                                t.ht()
                            elif turns==2:
                                t.pu()
                                t.rt(-90)
                                t.setx(-100)
                                t.sety(110)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==1:
                                t.pu()
                                t.rt(-45)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.ht()
                            elif turns==0:
                                t.pu()
                                t.rt(180)
                                t.setx(-100)
                                t.sety(135)
                                t.pd()
                                t.fd(30)
                                t.pu()
                                t.ht()
                                time.sleep(1)
                                print("You Lost")
                                print("The place was ",word)
                                t.clear()
                                m.clear()
                                t.color("red")
                                t.write("You Lost! :(",move=False,align="center",font=("Calibri",60,"normal"))
                                time.sleep(3)
                                t.clear()
                                m.clear()
                                break
                    
            else:
                print("Invalid Input")
            t.ht()
            wn.reset()
                            
        


                
                
                        
                    
    

