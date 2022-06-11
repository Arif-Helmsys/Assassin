from Pydate import PyDate
from util import Console
import sys
from getpass import getuser
import os

__version__ = 0.1
__version__link__ = "https://raw.githubusercontent.com/Arif-Helmsys/Assassin/main/version.json"
class VersionControl(PyDate):
    def __init__(self, path: str, rawlink: str) -> None:
        super().__init__(path, rawlink, isScript=True)
        if not os.path.exists(f"{os.getcwd()}\\version.json"):
            self.control()
        if not self.isUpdate:
            while True:
                _input = Console._input_(self,f"{Console.CYAN}╭──({Console.BOLD}{Console.PURPLE}assassin@{getuser().lower()}{Console.CYAN})~[New Update Available! (Y/n)]{Console.DEFAULT}{Console.CYAN}\n╰──────{Console.RED}{Console.BOLD}# ")
                if _input == "Y":
                    self.saveNewVersion(False)
                    self.scriptUpdate()
                    print(f"\t{Console.CYAN}╰──/UPDATED!{Console.DEFAULT}".expandtabs(7))
                    sys.exit(0)
                elif _input == "n":
                    print(f"\t{Console.CYAN}╰──/Please Updated{Console.DEFAULT}".expandtabs(7))
    
    def scriptUpdate(self) -> bool:
        script__raw_link = "https://raw.githubusercontent.com/Arif-Helmsys/Assassin/main/assassin.py"
        return super().scriptUpdate(script__raw_link, "assassin")

    def control(self):
        return self.createVersionFile(__version__)


if __name__ != "__main__":
    v = VersionControl(path=os.getcwd(),rawlink=__version__link__)
