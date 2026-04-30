import os
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
{NEON_PURPLE}         ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌{RESET}
{NEON_BLUE}         ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌{RESET}
{NEON_GREEN}         ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓{RESET}
{NEON_CYAN}         ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒{RESET}
{NEON_PINK}           ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒{RESET}
{NEON_PURPLE}           ░░   ░   ░   ▒    ▒ ░ ░ ░  ░{RESET}
{NEON_BLUE}               ░           ░  ░ ░     ░{RESET}
{NEON_GREEN}                        ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Option 1{RESET}
{NEON_PURPLE}[2] Option 2{RESET}
"""

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)
    print(menu2)

def main():
    while True:
        show_menu()
        try:
            choice = int(input(f"{NEON_RED}Choice >> {RESET}"))
            if choice == 0:
                break
            else:
                print(f"{NEON_RED}This option is disabled in the safe version.{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{NEON_RED}Please enter a valid number{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
