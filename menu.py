import os
import time

def intro():
    l = []
    l.append(" ______     ______     ______   ______   __         ______     ______     __  __     __     ______  ")
    l.append("/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  == \ ")
    l.append("\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ ")
    l.append(" \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   ")
    l.append("  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   ")
    l.append("                                                                                                    ")
    l.append("                                                  # #  ( )                                          ")
    l.append("                                               ___#_#___|__                                         ")
    l.append("                                           _  |____________|  _                                     ")
    l.append("                                    _=====| | |            | | |==== _                              ")
    l.append("                              =====| |.---------------------------. | |====                         ")
    l.append("                <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  ")
    l.append("                  \                                                             /                   ")
    l.append("                   \___________________________________________________________/                    ")
    l.append("               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ")
    l.append("             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               ")
    l.append("                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 ")
    for i in range(1, len(l[0]) + 1): 
        for j in l:
            print(j[-i:])  
intro()


def menu():
    print("\n\n\nWelcome to Beke-Vadászhajó!\n\n\n")
    print("Good Luck & Happy Easter!")
    print("\n\n\n")
menu()
