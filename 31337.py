#/env/python3.8
#-----! partner box debuger !------#
from netcat import Netcat
import ast
import sys


log = ("""
██████   █████  ██████  ████████ ███    ██ ███████ ██████  ██████  ██████  ██████  
██   ██ ██   ██ ██   ██    ██    ████   ██ ██      ██   ██ ██   ██      ██ ██   ██ 
██████  ███████ ██████     ██    ██ ██  ██ █████   ██████  ██   ██  █████  ██████  
██      ██   ██ ██   ██    ██    ██  ██ ██ ██      ██   ██ ██   ██      ██ ██   ██ 
██      ██   ██ ██   ██    ██    ██   ████ ███████ ██   ██ ██████  ██████  ██████  
                                                                                   
        A Partner box Debuger Made by ibaraky https://github.com/ibarkay
                example : python3 31337.py -h 192.168.1.60
""")

fily = open('31337.txt','r').readlines()

until = 'Success'
try:
    HOST = sys.argv[sys.argv.index("-h") + 1] #HOST = "192.168.1.60"
except:
    print("Please insert host with -h , example : -h 192.168.1.60")


PORT = 31337
nc = Netcat(HOST,PORT)

COMMANDS = [x.replace('\n','') for x in fily]
COMMANDS = [ast.literal_eval(x) for x in COMMANDS]
#print(COMMANDS)
listCmds = []
run = True

def list_cmds():
    if len(listCmds) == 0:
        for i in COMMANDS:
            listCmds.append(i[0])
    else:
        pass

def Run():
    global run
    num = 0
    num2 = 0
    Cmd = ""
    for i in listCmds:
        print("{} - for {}".format(num,str(i).replace('[', '').replace(']', '').replace('\'', '')))
        num += 1
    print('99 - for exit')

    userInput = input("Please make your choise : ")
    if int(userInput) == 99 :
        run = False
    else:
        Cmd += str(COMMANDS[int(userInput)][0])

        for elm in COMMANDS[int(userInput)][1]:
            print("{}  for {}".format(num2, elm))
            num2 += 1
        print('99 - for exit')

        userInput2 = input("--- {} ---Please make your choise : ".format(Cmd.replace('[', '').replace(']', '').replace('\'', '')))
        if int(userInput2) == 99:
            run = False
        else:
            Cmd += " " + str(COMMANDS[int(userInput)][1][int(userInput2)])
            CmdFinal = Cmd.replace('[', '').replace(']', '').replace('\'', '')
            print(CmdFinal)
            nc.write(CmdFinal)
            print(nc.read_until(until))
            a = input("Press any key to continue")


if __name__ == '__main__':
    print("\033[1;32;32m" + log + "\033[m")
    list_cmds()
    while run:
        Run()
