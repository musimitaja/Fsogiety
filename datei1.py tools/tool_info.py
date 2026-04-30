import os

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

def load_config(filename):
    config = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        config["error"] = "config.txt not found"
    return config

config = load_config('config.txt')

menu = f"""
{NEON_CYAN}         ▄▄▄█████▓ ▒█████   ▒█████   ██▓        ██▓ ███▄    █   █████▒▒█████{RESET}
{NEON_PINK}         ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒{RESET}
{NEON_PURPLE}         ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒{RESET}
{NEON_BLUE}         ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░{RESET}
{NEON_GREEN}           ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░{RESET}
{NEON_CYAN}           ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░{RESET}
{NEON_PINK}             ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░{RESET}
{NEON_PURPLE}            ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒{RESET}
{NEON_BLUE}                     ░ ░      ░ ░      ░  ░    ░           ░            ░ ░{RESET}
"""

menu2 = f"""
{NEON_PINK}> Tool Name     : {NEON_CYAN}DARK NEXUS{RESET}
{NEON_PINK}> Version       : {NEON_CYAN}BETA{RESET}
{NEON_PINK}> Creator       : {NEON_CYAN}JUSTNUTELABROT{RESET}
{NEON_PINK}> Coding        : {NEON_CYAN}PRIVST{RESET}
{NEON_PINK}> Discord [W]   : {NEON_CYAN}JUSTNUTELLABROT{RESET}
{NEON_PINK}> GitHub [W]    : {NEON_CYAN}MUSIMITAJA{RESET}
"""

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)
    print(menu2)

if __name__ == "__main__":
    show_menu()
    input(f"\n{NEON_CYAN}Press Enter to return to the main menu...{RESET}")
    os.system('python cyb3rtech.py')
