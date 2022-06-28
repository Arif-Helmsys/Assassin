import sys
from time import sleep
import random
import os

class Console:
    PURPLE    = '\033[95m'
    CYAN      = '\033[96m'
    DARKCYAN  = '\033[36m'
    BLUE      = '\033[94m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    BOLD      = '\033[1m'
    DEFAULT   = '\033[0m'
    SHAKER = [PURPLE,RED,CYAN,YELLOW,GREEN]

    #----------------------CONSOLE COMMANDS-----------------#
    SHUTDOWN = "sdown"
    CONNECT = "conn"
    MY_SHELL = "m-shell"
    EXECUTE = "c_exe"
    HELP = "help"
    HELPER = f"""\t\t\t {CYAN}╰──/{DEFAULT}{SHUTDOWN}{CYAN}    [{GREEN}Shutdown{CYAN}]
       ╰──/{DEFAULT}{CONNECT}{CYAN}     [{GREEN}Connect{CYAN}]
       ╰──/{DEFAULT}{MY_SHELL}{CYAN}  [{GREEN}My-Shell{CYAN}]
       ╰──/{DEFAULT}{EXECUTE}{CYAN}    [{GREEN}Creating Execute{CYAN}]""".expandtabs(2)
    #----------------------CONSOLE COMMANDS-----------------#

    def _input_(self,string:str) -> str:
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
        return input()

    def loadingAnimation(self):
        load_str = "connecting "
        ls_len = len(load_str)
        animation = "|/-\\"
        anicount = 0
        counttime = 0
        i = 0
        r = random.randint(20,30)
        while (counttime != r):
            sleep(0.075) 
            load_str_list = list(load_str)   
            x = ord(load_str_list[i])
            y = 0                             
            if x != 32 and x != 46:             
                if x>90:
                    y = x-32
                else:
                    y = x + 32
                load_str_list[i]= chr(y)
            res =''             
            for j in range(ls_len):
                res = res + load_str_list[j]
            sys.stdout.write("\r"+res + animation[anicount])
            load_str = res
            anicount = (anicount + 1)% 4
            i =(i + 1)% ls_len
            counttime = counttime + 1

if __name__ != "__main__":
    os.system("cls")