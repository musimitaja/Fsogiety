import requests
import os
import sys

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

menu = f"""
{NEON_CYAN}         ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███{RESET}
{NEON_PINK}         ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒{RESET}
{NEON_PURPLE}          ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒{RESET}
{NEON_BLUE}         ░  ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄{RESET}
{NEON_GREEN}           ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒{RESET}
{NEON_CYAN}           ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░{RESET}
{NEON_PINK}           ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░{RESET}
{NEON_PURPLE}           ░         ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░{RESET}
{NEON_BLUE}                  ░           ░  ░░ ░      ░  ░      ░  ░   ░{RESET}
"""

menu2 = f"""
{NEON_CYAN}[0] Back to main{RESET}
{NEON_PINK}[1] Username Tracker{RESET}
"""

def show_menu():
    print(menu)
    print(menu2)

def username_tracker(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "PayPal": f"https://www.paypal.me/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Guns.lol": f"https://guns.lol/{username}",
        "Flickr": f"https://www.flickr.com/photos/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "RedBubble": f"https://www.redbubble.com/people/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
    }

    print(f"{NEON_CYAN}Checking usernames for '{username}'...{RESET}")

    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{NEON_GREEN}[+] {site}: {url}{RESET}")
            else:
                print(f"{NEON_RED}[-] {site}: {url}{RESET}")
        except requests.RequestException:
            print(f"{NEON_RED}[-] {site}: {url}{RESET}")

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
                user = input(f'{NEON_RED}Pseudo >> {RESET}')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(menu)
                username_tracker(user)
            else:
                print(f"{NEON_RED}[!]{RESET} Invalid choice {NEON_RED}[!]{RESET}")
        except ValueError:
            print(f"{NEON_RED}Please enter a valid number{RESET}")
        input(f"\n{NEON_CYAN}Press Enter to return to the menu...{RESET}")

if __name__ == "__main__":
    main()
