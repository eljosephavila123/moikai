import platform

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▐─▌──▐─▌──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}System: {platform.system()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐▌─▐▌▐▌─▐▌─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Name: {platform.uname()[0]}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─█▄▀▄██▄▀▄█─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Platform: {platform.uname()[0]}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▄──██▌─▄──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Version: { platform.version()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▄▀─█▀██▀█─▀▄{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Processor: {platform.processor()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▐▌▐▌─▐▌─▐▌▐▌{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Machine: {platform.machine()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐─█────█─▌─{bcolors.ENDC}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    -───▌──▐────{bcolors.ENDC}")


