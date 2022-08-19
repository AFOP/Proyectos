#!/usr/bin/python3
'''
move_quizc: object moves when answered correctly 
'''
from colorama import init, Fore, Back, Style
import os
import time

i = 0
speed = 0
form = "O^o"
print(Fore.YELLOW + "Welcome to the race Holberton 2022")
print("=============================================")
value = input(Fore.WHITE + "Please enter the speed of the bike: ")
print(value)
print("=============================================")
value = int(value)
if (value > 15):
    value = 15
while (i < value):
    os.system("clear")
    speed += i
    spaces = (" " * speed)
    street = ("===" * 40)
    time.sleep(0.1)
    print(Fore.YELLOW + f"{street}" + Fore.RESET)
    print(Fore.BLUE + f"{spaces} {form} {Fore.RESET}")
    print(Fore.YELLOW + f"{street}" + Fore.RESET)
    i = i + 1 
