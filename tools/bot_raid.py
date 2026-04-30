import os
import time

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_PINK}         ██▀███   ▄▄▄       ██▓▓█████▄{RESET}
{NEON_CYAN}         ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌{RESET}
{NEON_PURPLE}       ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌{RESET}
{NEON_BLUE}         ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌{RESET}
{NEON_GREEN}        ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓{RESET}
{NEON_PINK}         ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒{RESET}
{NEON_CYAN}           ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒{RESET}
{NEON_PURPLE}           ░░   ░   ░   ▒    ▒ ░ ░ ░  ░{RESET}
{NEON_BLUE}               ░           ░  ░ ░     ░{RESET}
{NEON_GREEN}                        ░{RESET}
{NEON_PINK}              >> (Bot Version) <<{RESET}
"""

menu2 = f"""
{NEON_CYAN}  [0] Back to main{RESET}
{NEON_PINK}  [1] Nuke{RESET}
{NEON_PURPLE}[2] Message Spam{RESET}
{NEON_BLUE}  [3] Delete Channel{RESET}
{NEON_GREEN} [4] Create Channel{RESET}
{NEON_CYAN}  [5] Create Role{RESET}
{NEON_PINK}  [6] Delete Role{RESET}
"""

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)
    print(menu2)

def main():
    while True:
        show_menu()
        choice = input(f"{NEON_PINK}Choice >> {RESET}")
        if choice == "0":
            break
        elif choice in {"1", "2", "3", "4", "5", "6"}:
            print(f"{NEON_RED}This option is disabled in the safe neon version.{RESET}")
            time.sleep(1.2)
        else:
            print(f"{NEON_RED}[!] Invalid choice{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
