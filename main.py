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

##change players
def crUser(cp,players):
    if cp==players[0]:
        return players[1]
    else:
        return players[0]
##board
def b_board():
    table1=[[1,2,3],[4,5,6],[7,8,9]]
    table2=[[1,2,3],[4,5,6],[7,8,9]]
    table3=[[1,2,3],[4,5,6],[7,8,9]]
    rows=3
    cols=3
    tables=3
    for z in range(3):
        print(f'Table {z} ')
        for x in range(rows):
            print("\n+---+---+---+")
            print("|", end="")
            for y in range(cols):
                print("", " ",end=" |")
        print("\n+---+---+---+")
#    print(table1,table2,table3)
    opt=["", "", "", "", "", "", "", "", ""]


##place new move
def move():
    pass
##check win
def is_Win():
 pass

##winners board -how to do file?
def winners_B(cp):
    winnerdic={}
    if cp not in winnerdic.key:
        winnerdic.setdefault(cp,1)
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
    b_board()
    while  is_Win()!="yes":
        move()
        is_Win()
        cp=crUser(cp,players)
        print(f'now the new user is: {cp}')
    print("""
            dP   dP   dP dP 888888ba  888888ba   88888888b  888888ba  
            88   88   88 88 88    `8b 88    `8b  88         88    `8b 
            88  .8P  .8P 88 88     88 88     88 a88aaaa    a88aaaa8P' 
            88  d8'  d8' 88 88     88 88     88  88         88   `8b. 
            88.d8P8.d8P  88 88     88 88     88  88         88     88 
            8888' Y88'   dP dP     dP dP     dP  88888888P  dP     dP 
            oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            """)
    winners_B()
    print("== WINNER | WINS ===")
    for key,value in winners_B():
        print(f'{key} | {value} end=""')
b_board()
#main()

