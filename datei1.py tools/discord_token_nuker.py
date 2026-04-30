import os
import requests
import json
import time
from datetime import datetime, timezone

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ██▓ ███▄    █   █████▒▒█████{RESET}
{NEON_PINK}         ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒{RESET}
{NEON_PURPLE}         ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒{RESET}
{NEON_BLUE}         ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░{RESET}
{NEON_GREEN}           ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░{RESET}
{NEON_CYAN}           ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░{RESET}
{NEON_PINK}             ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░{RESET}
{NEON_PURPLE}           ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒{RESET}
{NEON_BLUE}                  ░ ░  ░  ░      ░  ░         ░     ░           ░            ░ ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Token Info{RESET}
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
            elif choice == 1:
                print(f"{NEON_RED}Token info mode is disabled here.{RESET}")
            else:
                print(f"{NEON_RED}[!] > Invalid choice < [!]{RESET}")
        except ValueError:
            print(f"{NEON_RED}[!] Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the main menu...{RESET}")

if __name__ == "__main__":
    main()
