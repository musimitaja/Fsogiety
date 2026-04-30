import os
import re
import dns.resolver

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ██▓ ███▄    █   █████▒▒█████{RESET}
{NEON_PINK}         ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒{RESET}
{NEON_PURPLE}       ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒{RESET}
{NEON_BLUE}         ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░{RESET}
{NEON_GREEN}        ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░{RESET}
{NEON_CYAN}         ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░{RESET}
{NEON_PINK}         ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░{RESET}
{NEON_PURPLE}         ░      ░     ░   ▒    ▒ ░  ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒{RESET}
{NEON_BLUE}                ░         ░  ░ ░      ░  ░    ░           ░            ░ ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Email Info{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None

    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = resolver.resolve(domain_all, 'MX')
        info["mx_servers"] = [str(record.exchange) for record in mx_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["mx_servers"] = None

    try:
        spf_records = resolver.resolve(domain_all, 'SPF')
        info["spf_records"] = [str(record) for record in spf_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["spf_records"] = None

    try:
        dmarc_records = resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record) for record in dmarc_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["dmarc_records"] = None

    if info.get("mx_servers"):
        for server in info["mx_servers"]:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server:
                info["microsoft_365"] = True

    return info, domain_all, domain, tld, name

def email_info():
    email = input(f"{NEON_RED}Email >> {RESET}")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)

    info, domain_all, domain, tld, name = get_email_info(email)

    mx_servers = ' / '.join(info["mx_servers"]) if info.get("mx_servers") else None
    spf_records = ' / '.join(info["spf_records"]) if info.get("spf_records") else None
    dmarc_records = ' / '.join(info["dmarc_records"]) if info.get("dmarc_records") else None
    google_workspace = info.get("google_workspace", None)

    print(f"""
{NEON_CYAN}
    [+] Email      : {email}
    [+] Name       : {name}
    [+] Domain     : {domain}
    [+] Tld        : {tld}
    [+] Domain All : {domain_all}
    [+] Servers    : {mx_servers}
    [+] Spf        : {spf_records}
    [+] Dmarc      : {dmarc_records}
    [+] Workspace  : {google_workspace}
{RESET}
    """)

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
                email_info()
            else:
                print(f"{NEON_RED}[!] Invalid choice [!]{RESET}")
        except ValueError:
            print(f"{NEON_RED}Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the menu...{RESET}")

if __name__ == "__main__":
    main()
