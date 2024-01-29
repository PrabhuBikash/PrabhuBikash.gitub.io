print("                  \033[1;4;36mMADE BY PRABHUBIKASH\033[0m😎  \n\033[1;4mTIC-TAC-TOE :\nRULES :\033[0;1m\n1.\033[0m Players take turns to enter their move. The default markers are X and O.\n\033[1m2.\033[0m To make a move, enter the corresponding number where you want to place your symbol.\n\033[1m3.\033[0m The game will notify you if a move is invalid (already occupied or out of range).\n\033[1m4.\033[0m The first player to complete a line of three of their symbols wins the game.\n\033[1m5.\033[0m If the board is filled, and no player has three in a row, the game is a draw.\n\033[1;36m\n                 |     |    \n              1  |  2  |  3  \n            _____|_____|_____\n                 |     |     \n              4  |  5  |  6  \n            _____|_____|_____\n                 |     |     \n              7  |  8  |  9  \n                 |     |     \n\033[0m")
def Choose():
    N=input("(enter for default : X) Marker of 1st player : ")
    if not N:
        N="X"
    print("(enter for default :","O) Marker of 2nd player : " if N!="O" else "X) Marker of 2nd player : ",end="")
    M=input()
    if not M :
        M="O" if N!="O" else "X"
    return [N,M] if N!=M else [print("same same!!🧐 "),Choose()][1]
def Draw(v):
    while True:
        try:
            n=int(input())
            if n in v:
                v.remove(n)
            return n if 0<n<10 else int("E")
        except ValueError:
            print(f"\033[31;1mEnter a number from \033[0;1m{v}\033[0m")
def Placeholder():
    p=(input("Do you want to display move numbers? (Y / N) : ").upper()).replace(" ","")
    return True if p=="Y" or p=="YES" or p=="Y " or p=="YES " else False if p=="N" or p=="NO" else [print("\033[1;31mYES OR NO!?\033[0m"),Placeholder()][1]
def Assign(n,x,v,L):
    if L[n]=="":
        L[n]=x
        return False
    else:
        print(f"\033[31;1malready occupied choose a number from\033[0;1m{v}\033[0m")
        return True
def Check(x,L):
    B=[[L[1],L[2],L[3]],[L[4],L[5],L[6]],[L[7],L[8],L[9]],[L[1],L[4],L[7]],[L[2],L[5],L[8]],[L[3],L[6],L[9]],[L[1],L[5],L[9]],[L[3],L[5],L[7]]]
    return True if any(all(j==x for j in i) for i in B) else False
def Align(x,s):
    return " "*s if x=="" else " "*((s-len(str(x)))//2)+str(x)+" "*((s-len(str(x)))-(s-len(str(x)))//2)
def Print1(L,s):
    print("\033[1;4mTIC-TAC-TOE :\033[0m\n\033[1;36m\n            "+" "*s+"    |    "+" "*s+"|\n              "+Align(L[1],s)," |  "+Align(L[2], s)," |  "+Align(L[3],s)+"\n            __"+"_"*s+"__|__"+"_"*s+"__|__"+"_"*s+"__\n            "+" "*s+"    |    "+" "*s+"|\n              "+Align(L[4],s)," |  "+Align(L[5],s)," |  "+Align(L[6],s)+"\n            __"+"_"*s+"__|__"+"_"*s+"__|__"+"_"*s+"__\n            "+" "*s+"    |    "+" "*s+"|\n              "+Align(L[7],s)," |  "+Align(L[8],s)," |  "+Align(L[9],s)+"\n            "+" "*s+"    |    "+" "*s+"|\n\033[0m")
def Print2(L,s):
    print("\033[1;4mTIC-TAC-TOE :\033[0m\n\033[1;36m\n            "+" "*s+"    |    "+" "*s+"|\n             ",f"\033[0;2;37m1\033[0;{Align(1,s)};36m" if L[1]=="" else Align(L[1],s)," | ",f"\033[0;2;37m{Align(2,s)}\033[0;1;36m" if L[2]=="" else Align(L[2],s)," | ",f"\033[0;2;37m{Align(3,s)}\033[0;1;36m" if L[3]=="" else Align(L[3],s),"\n            __"+"_"*s+"__|__"+"_"*s+"__|__"+"_"*s+"__\n            "+" "*s+"    |    "+" "*s+"|\n             ",f"\033[0;2;37m{Align(4,s)}\033[0;1;36m" if L[4]=="" else Align(L[4],s)," | ",f"\033[0;2;37m{Align(5,s)}\033[0;1;36m" if L[5]=="" else Align(L[5],s)," | ",f"\033[0;2;37m{Align(6,s)}\033[0;1;36m" if L[6]=="" else Align(L[6],s),"\n            __"+"_"*s+"__|__"+"_"*s+"__|__"+"_"*s+"__\n            "+" "*s+"    |    "+" "*s+"|\n             ",f"\033[0;2;37m{Align(7,s)}\033[0;1;36m" if L[7]=="" else Align(L[7],s)," | ",f"\033[0;2;37m{Align(8,s)}\033[0;1;36m" if L[8]=="" else Align(L[8],s)," | ",f"\033[0;2;37m{Align(9,s)}\033[0;1;36m" if L[9]=="" else Align(L[9],s),"\n            "+" "*s+"    |    "+" "*s+"|\n\033[0m")
def Play():
    D,L,V,t,P=Choose(),[""]*10,[1,2,3,4,5,6,7,8,9],0,Placeholder()
    while t<9:
        print(f"{D[0]}'s chance : ")
        if (Assign(Draw(V),D[0],V,L)):
            continue
        else:
            if P:
                Print2(L,max(map(len, D)))
            else:
                Print1(L,max(map(len, D)))
            t+=1
            if Check(D[0],L):
                t=10
                print(f"\033[1;32m            {D[0]} is the winner🥳 \033[0m")
            else:
                D.reverse()
    print("\033[1;33m                DRAW\033[0m\n" if t==9 else "",end="")
Play()
while input('\n WANNA PLAY AGAIN! \n (type"NO" to end else type something/enter to play) : ').upper()!="NO":
    Play()
print("\n                    GAME ENDED\n\n© ALL COPY RIGHTS RESERVED")