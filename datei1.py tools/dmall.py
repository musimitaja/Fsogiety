import os
import requests
import time

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ▓█████▄  ███▄ ▄███▓ ▄▄▄       ██▓     ██▓{RESET}
{NEON_PINK}         ▒██▀ ██▌▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓██▒{RESET}
{NEON_PURPLE}         ░██   █▌▓██    ▓██░▒██  ▀█▄  ▒██░    ▒██░{RESET}
{NEON_BLUE}         ░▓█▄   ▌▒██    ▒██ ░██▄▄▄▄██ ▒██░    ▒██░{RESET}
{NEON_GREEN}         ░▒████▓ ▒██▒   ░██▒ ▓█   ▓██▒░██████▒░██████▒{RESET}
{NEON_CYAN}         ▒▒▓  ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░{RESET}
{NEON_PINK}           ░ ▒  ▒ ░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░{RESET}
{NEON_PURPLE}           ░ ░  ░ ░      ░     ░   ▒     ░ ░     ░ ░{RESET}
{NEON_BLUE}             ░           ░         ░  ░    ░  ░    ░  ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Dmall Friends (SelfBot){RESET}
{NEON_PURPLE}[2] Dmall Dm Open (SelfBot){RESET}
{NEON_BLUE}[3] Dmall Server (Bot){RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input(f'{NEON_RED}Choice >> {RESET}'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            else:
                print(f"{NEON_RED}This option is disabled in the safe neon version.{RESET}")
        except ValueError:
            print(f"{NEON_RED}[!] Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the main menu...{RESET}")

if __name__ == "__main__":
    main()
