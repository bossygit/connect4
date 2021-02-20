from termcolor import colored, cprint
table = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
col = 13
row = 6
l = len(table)
x = colored('x', 'red')
o = colored('o', 'yellow')


def win(tab,play):
    for six in range(6):
        count = 0
        for s in range(5,-1,-1):
            if tab[s][six] == play:
                count += 1
                if count == 4:
                    print("You win")
                    return True
            if tab[s][six] != play:
                count = 0
def wino(tab,play):
    start = 0
    end = 4
    for master in range(4):
        for it in range(5, 2, -1):
            temp = it
            count = 0
            for i in range(start, end):
                if tab[temp][i] == play:
                    count += 1
                    if count == 4:
                        print("You win")
                        return True
                if tab[temp][i] != play:
                    count = 0
                temp -= 1

        start += 1
        end += 1

def winy(tab,play):
    start = 6
    end = 2
    for master in range(3):
        for it in range(5, 2, -1):
            temp = it
            count = 0
            for i in range(start, end,-1):
                if tab[temp][i] == play:
                    count += 1
                    if count == 4:
                        print("You win")
                        return True
                if tab[temp][i] != play:
                    count = 0

                temp -= 1

        start -= 1
        end -= 1

def winline(tab,play):
    for horizontal in range(6):
        count = 0
        for line in range(7):
            if tab[horizontal][line] == play:
                count += 1
                if count == 4:
                    print("You win")
                    return True
            if tab[horizontal][line] != play:
                count = 0

def showfour(tbl):
    for r in range(row):
        tour = 0
        for c in range(col):
            if c%2 == 0:
                print("{}".format(tbl[r][tour]),end="")
                tour += 1
            else:
                print("|",end="")
        print("")
        print("-------------")
# A player can enter 7 possible number from 0 to 6
player = 1
jouer1 = ""
jouer2 = ""
while(True):
    if(player == 1):
        print("Player 1 is playing")
        choice = int(input("Enter the column from O to 6 : "))
        point = "o"
        for t in range(l-1,-1,-1):
            if table[t][choice] == " ":
                table[t][choice] = o
                break
        showfour(table)
        player = 2
        print(" Changing player ... " + str(player))
        if win(table,o):
            break
        if wino(table,o):
            break
        if winy(table,o):
            break
        if winline(table,o):
            break


    if(player == 2):
        print("Player 2 is playing")
        choice = int(input("Enter the column from O to 6 : "))
        for t in range(l-1,-1,-1):
            if table[t][choice] == " ":
                table[t][choice] = x
                break
        showfour(table)
        player = 1
        print(" Changing player ... " + str(player))
        if win(table,o):
            break
        if wino(table,o):
            break
        if winy(table,o):
            break
        if winline(table,o):
            break
