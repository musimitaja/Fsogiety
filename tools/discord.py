import os
import webbrowser
import time

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}             ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄{RESET}
{NEON_PINK}             ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌{RESET}
{NEON_PURPLE}           ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌{RESET}
{NEON_BLUE}             ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌{RESET}
{NEON_GREEN}            ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓{RESET}
{NEON_CYAN}             ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒{RESET}
{NEON_PINK}             ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒{RESET}
{NEON_PURPLE}             ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░{RESET}
{NEON_BLUE}             ░     ░        ░  ░ ░          ░ ░     ░        ░{RESET}
{NEON_GREEN}             ░                   ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

time.sleep(1)
webbrowser.open('https://discord.gg/mP6NvAgF2q')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input(f'{NEON_PINK}Choise >> {RESET}'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            else:
                print(f"{NEON_RED}[!] >{RESET} Invalid choice {NEON_RED}< [!]{RESET}")
        except ValueError:
            print(f"{NEON_RED}[!] Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the main menu...{RESET}")

if __name__ == "__main__":
    main()
