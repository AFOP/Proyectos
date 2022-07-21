#!/usr/bin/python3
'''
shell command questions 
'''
from colorama import init, Fore, Back, Style

score=0
i=0
questions=[
    "Which command should you use to display the current path of your current directory?",
    "Which command should you use to list all files of your current directory?",
    "Which command should you use to change directory?",
    "Which command should you use to display the content of a file?",
    "Which command should you use to create an empty file?",
    "Which command should you use to copy a file (or directory if additional argument)?",
    "Which command should you use to rename or move a file (or directory)?",
    "Which command should you use to delete a file (or directory if additional argument)?",
    "Which command should you use to create a directory?",
    "Which command should you use to delete a directory?"]
answers=["pwd","ls","cd","less","touch","cp","mv","rm","mkdir","rmdir"]
competitor=input("Ingrese su Nombre: ")

while i<10:
    print()
    print(Fore.WHITE+questions[i])
    user=input(Fore.WHITE+"Digite su respuesta: ")
    if answers[i] == user:
        print(Fore.GREEN+"Respuesta correcta")
        score = score + 1
    else:
        print(Fore.RED+"Respuesta incorrecta")
    i = i + 1
print(Fore.YELLOW+"Felicitaciones {:s} su puntaje es: {:d}".format(competitor, score))