""" פונקציה ראשונה - לוקחת את השני שמות שהוכנסו כבר דוחפת לליסט, עושה ראנדום ומחזירה את השם הנבחר
 פונקציה שמחליפה בין שחקן לשחקן
 פונקציה שיוצרת את הלוח
 פונקציה שממקמת את הבחירה של השחקן על הלוח
 פונקציה שבודקת ניצחון
 פונקציה שסופרת 60 שניות
פונקציה ששומרת לתוך רשימה של זוכים"""
import random
import re


##insert two names into list
def pName():
 player1=input("Player 1 please enter your name:")
 player2=input("Player 2 please enter your name:")
 players=[player1,player2]
 return players

##random first player
def radPlayer(players):
    cp=random.choice(players)
    return cp

##player's choice:
def choose_w(players):
    x=True
    while x==True:
        opt=["💧","🔥","☣️","🍄"]
        print(f'You can choose from follow:\n 1-{opt[0]}\t2-{opt[1]}\t3-{opt[2]}\t4-{opt[3]}')
        p1chose=int(input(f'{players[0]} Your choice:'))-1
        p2chose=int(input(f'{players[1]} Your choice:'))-1
        if p1chose!=p2chose:
            sure=input("are you sure? y/n")
            if sure=="y" or "Y":
                p1chose=opt[p1chose]
                p2chose=opt[p2chose]
                playerchoice={players[0]:p1chose,players[1]:p2chose}
                x=False
            else:
                 x=True
        else:
            print("CANT BE THE SAME")

    return playerchoice

##change players
def crUser(cp,players):
    if cp==players[0]:
        return players[1]
    else:
        return players[0]

#print boards
def create_boards():
    tables=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
    return tables

##boards
def print_boards(tables):

    for z in range(3):
        print(f'===Table {z+1}===')
        print()
        for x in range(3):
            print("\n+---+---+---+")
            print("|",end="")
            for y in range(3):
                print(" ",tables[x][y][z],end=" |")
        print("\n+---+---+---+")

##place new move
def move(tables,playerchoice,cp):
 print(f'Now it is {cp} turn ')
 x=False
 while x==False:
     newmovet=int(input("Choose boards:(1,2,3)"))-1
     newmover=int(input("Now Choose Row:(1-3 up to down)"))-1
     newmovec=int(input("Now Choose Colomn:(1-3 left to right)"))-1
     if tables[newmovet][newmovec][newmover]!="":
         print("Already taken,try again")
         x=False
     else:
        tables[newmovet][newmovec][newmover]=playerchoice[cp]
        print(print_boards(tables))
        x=True

 return tables

##check win
def is_Win(boards,playerchoice,cp):
#there is algorith for this. dont know how
# Check for horizontal wins on each table
    for i in range(3):
        for j in range(3):
            if boards[i][j][0] == boards[i][j][1] == boards[i][j][2] == playerchoice[cp]:
                return True
        # Check for vertical wins
    for i in range(3):
        for j in range(3):
            if boards[i][0][j] == boards[i][1][j] == boards[i][2][j] == playerchoice[cp]:
                return True
        # Check for diagonal wins
    if boards[0][0][0] == boards[1][1][1] == boards[2][2][2] == playerchoice[cp]:
        return True
    if boards[0][0][2] == boards[1][1][1] == boards[2][2][0] == playerchoice[cp]:
        return True
    if boards[0][2][2] == boards[1][1][1] == boards[2][0][0] == playerchoice[cp]:
        return True
    if boards[2][0][2] == boards[1][1][1] == boards[0][2][0] == playerchoice[cp]:
        return True
    if boards[0][0][0] == boards[0][1][1] == boards[0][2][2] == playerchoice[cp]:
        return True
    if boards[0][0][0] == boards[1][0][1] == boards[2][0][2] == playerchoice[cp]:
        return True
    if boards[0][2][0] == boards[1][1][1] == boards[2][0][2] == playerchoice[cp]:
        return True
    if boards[0][2][2] == boards[1][2][1] == boards[2][2][0] == playerchoice[cp]:
        return True
    if boards[0][0][2] == boards[1][0][1] == boards[2][0][0] == playerchoice[cp]:
        return True
    if boards[0][2][2] == boards[1][2][1] == boards[2][2][0] == playerchoice[cp]:
        return True
    if boards[2][0][2] == boards[2][1][1] == boards[2][2][0] == playerchoice[cp]:
        return True
        # No win condition found
    return False

def win_Display():
    print("""
            dP   dP   dP dP 888888ba  888888ba   88888888b  888888ba  
            88   88   88 88 88    `8b 88    `8b  88         88    `8b 
            88  .8P  .8P 88 88     88 88     88 a88aaaa    a88aaaa8P' 
            88  d8'  d8' 88 88     88 88     88  88         88   `8b. 
            88.d8P8.d8P  88 88     88 88     88  88         88     88 
            8888' Y88'   dP dP     dP dP     dP  88888888P  dP     dP 
            oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            """)

##winners boards -how to do file?
def winners_B(cp):
    winnerdic={}
    if cp not in winnerdic.key:
       winnerdic.setdefault(cp,winnerdic=1)
    else:
        winnerdic.update(cp,+1)
    return winnerdic
def main():
    ans="y"
    while ans=="y":
        players=pName()
        ans=input(f'Players names are: \n===> {players[0]} and {players[1]} <===\n do you want to change name? \n(hint:press y/n)')
        if ans=="y" or ans=="Y" :
            print(f'Players names are: \n {players[0]} and {players[1]}\nGOOD LUCK')
        else:
            print("GOOD LUCK")
    cp=radPlayer(players)
    print(f'First player to play is:\n=== {cp} ===')
    playerchoice=choose_w(players)
    boards=create_boards()
    print_boards(boards)
    while  is_Win(boards,playerchoice,cp)==False:
        move(boards,playerchoice,cp)
        is_Win(boards,playerchoice,cp)
        cp=crUser(cp,players)
        print_boards(boards)
    win=win_Display()
    winners_B(cp)
    print("== WINNER | WINS ===")
    for key,value in winners_B():
        print(f'{key} | {value} end=""')

main()
