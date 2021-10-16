from random import choice
from os import system
import os
import time
from colorama import Fore, Back, Style
import sys

#checking if your python isn´t 2
if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

os.system("title t.me/undecryptable")
os.system('cls||clear')

print(f"""
{Fore.MAGENTA}
    
                                ▓██   ██  ██  ███▄    █ 
                                 ▒██  ██  ██  ██ ▀█   █
                                  ▒██ ██  ██  ██  ▀█ ██▒
                                  ░ ▐██▓░░██░ ██▒  ▐███▒
                                  ░ ██▒▓░░██░▒██░    ██░
                                   ██▒▒▒ ░▓  ░ ▒░   ▒ ▒  
                                 ▓██░▒░  ▒ ░░ ░░   ░ ▒░
                                 ▒ ▒ ░░   ▒ ░   ░   ░ ░ 
                                 ░ ░      ░           ░ 
                                 ░ ░ 
                                 
                                 
                                       {Fore.WHITE} Input Count
""")
count = input(Fore.MAGENTA + " root" + Fore.WHITE + "@" + Fore.MAGENTA + "yin" + Fore.WHITE + ":" + Fore.CYAN+"~" + Fore.WHITE+" ")
print(" ")
print("Generating...")
print(" ")

#by yin/Timer/Kevin

tokenlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
uidlet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(int(count)):
    uid = ''
    token = ''
    for i in range(int(6)):
        uid = uid + choice(uidlet)
        token = token + choice(tokenlet)
    gen = "https://www.instagram.com/_n/emaillogindlink?uid=" + uid + "&token=" + token + "&auto_send=0"
    print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]  " + Fore.MAGENTA + gen + Fore.WHITE)
    with open('generated.txt', 'a') as x:
                x.write(gen + '\n')