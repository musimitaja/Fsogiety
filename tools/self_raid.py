import os
import requests
import threading
import time

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ██▀███   ▄▄▄       ██▓▓█████▄{RESET}
{NEON_PINK}         ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌{RESET}
{NEON_PURPLE}       ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌{RESET}
{NEON_BLUE}         ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌{RESET}
{NEON_GREEN}        ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓{RESET}
{NEON_CYAN}         ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒{RESET}
{NEON_PINK}           ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒{RESET}
{NEON_PURPLE}           ░░   ░   ░   ▒    ▒ ░ ░ ░  ░{RESET}
{NEON_BLUE}               ░           ░  ░ ░     ░{RESET}
{NEON_GREEN}                        ░{RESET}
            {NEON_CYAN}>> (SelfBot Version) <<{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Nuke{RESET}
{NEON_PURPLE}[2] Message Spam{RESET}
{NEON_BLUE}[3] Delete Channel{RESET}
{NEON_GREEN}[4] Create Channel{RESET}
{NEON_CYAN}[5] Create Role{RESET}
{NEON_PINK}[6] Delete Role{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

def is_user_token_valid(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    return response.status_code == 200

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input(f'{NEON_RED}Choice >> {RESET}'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            elif choice in {1, 2, 3, 4, 5, 6}:
                print(f"{NEON_RED}This option is disabled in the safe neon version.{RESET}")
                time.sleep(1)
            else:
                print(f"{NEON_RED}[!] Invalid choice{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{NEON_RED}[!] Please enter a number{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
