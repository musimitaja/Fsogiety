import os
import requests
import threading
import time
import random
import string
from datetime import datetime

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █{RESET}
{NEON_PINK}         ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █{RESET}
{NEON_PURPLE}       ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒{RESET}
{NEON_BLUE}         ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒{RESET}
{NEON_GREEN}        ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░{RESET}
{NEON_CYAN}         ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒{RESET}
{NEON_PINK}         ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░{RESET}
{NEON_PURPLE}           ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░{RESET}
{NEON_BLUE}                 ░  ░              ░         ░ ░           ░    ░  ░         ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Nitro Generator{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

def log_with_time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{NEON_BLUE}[{current_time}]{RESET} {message}")

def check_nitro(nitro_code):
    response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{nitro_code}")
    return response.status_code, response.url

def send_webhook(webhook_url, message):
    requests.post(webhook_url, json={"content": message})

def generate_nitro_codes():
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        yield code

def nitro_generator():
    use_webhook = input(f'{NEON_PINK}Use Webhook? (y/n) >> {RESET}').strip().lower() == 'y'
    webhook_url = ''
    if use_webhook:
        webhook_url = input(f'{NEON_PINK}Webhook URL >> {RESET}').strip()
    num_threads = int(input(f'{NEON_PINK}Number of Threads >> {RESET}'))

    found = threading.Event()

    def check_codes():
        for code in generate_nitro_codes():
            if found.is_set():
                break
            status_code, url = check_nitro(code)
            full_url = f"https://discord.gift/{code}"
            if status_code == 200:
                log_with_time(f"{NEON_GREEN}[+] Valid Nitro Code: {full_url}{RESET}")
                if use_webhook:
                    send_webhook(webhook_url, f"Valid Nitro Code: {full_url}")
                found.set()
            else:
                log_with_time(f"{NEON_RED}[-] Invalid Nitro Code: {full_url}{RESET}")

    threads = [threading.Thread(target=check_codes) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

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
                nitro_generator()
            else:
                log_with_time(f"{NEON_RED}[!] Invalid choice{RESET}")
        except ValueError:
            log_with_time(f"{NEON_RED}[!] Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the main menu...{RESET}")

if __name__ == "__main__":
    main()
