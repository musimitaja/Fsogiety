import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import sys
import time
import os

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███{RESET}
{NEON_PINK}         ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒{RESET}
{NEON_PURPLE}       ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒{RESET}
{NEON_BLUE}         ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄{RESET}
{NEON_GREEN}        ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒{RESET}
{NEON_CYAN}         ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░{RESET}
{NEON_PINK}         ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░{RESET}
{NEON_PURPLE}         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░{RESET}
{NEON_BLUE}             ░    ░            ░    ░         ░  ░   ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Phone Number Tracker{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

def track_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number))
    try:
        parsed_number = phonenumbers.parse(f"+{phone_number}", None)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{NEON_RED}[!] Invalid phone number format [!]{RESET}")
            return

        number_info = {
            "Country": geocoder.description_for_number(parsed_number, 'en'),
            "ISP": carrier.name_for_number(parsed_number, 'en'),
            "Time Zone": ", ".join(timezone.time_zones_for_number(parsed_number)),
            "National Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "International Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "E.164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Number Type": phonenumbers.number_type(parsed_number),
            "Possible Number": phonenumbers.is_possible_number(parsed_number)
        }

        print(f"{NEON_RED}Recherche pour le numéro '+{phone_number}'..{RESET}")
        time.sleep(2)
        for key, value in number_info.items():
            print(f"{NEON_CYAN}{key}: {NEON_PINK}{value}{RESET}")

    except phonenumbers.NumberParseException:
        print(f"{NEON_RED}[!] Failed to parse phone number [!]{RESET}")

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
                phone_number = input(f'{NEON_RED}Phone Number >> {RESET}')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(menu)
                track_phone_number(phone_number)
            else:
                print(f"{NEON_RED}[!]{RESET} Invalid choice {NEON_RED}[!]{RESET}")
        except ValueError:
            print(f"{NEON_RED}Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the menu...{RESET}")

if __name__ == "__main__":
    main()
