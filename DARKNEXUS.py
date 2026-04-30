import os
import time
import shutil

NEON_PINK = "\033[38;2;255;0;180m"
NEON_CYAN = "\033[38;2;0;255;255m"
NEON_PURPLE = "\033[38;2;180;0;255m"
NEON_GREEN = "\033[38;2;0;255;120m"
NEON_BLUE = "\033[38;2;80;160;255m"
NEON_RED = "\033[38;2;255;60;60m"
RESET = "\033[0m"

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    return "\n".join(line.center(width) for line in lines)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def blinking():
    text = f"""
{NEON_PINK}  ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗{RESET}
{NEON_CYAN}  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██████╔╝{RESET}
{NEON_PURPLE}██║  ██║███████║██████╔╝█████╔╝     ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗{RESET}
{NEON_BLUE}  ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║{RESET}
{NEON_GREEN} ██████╔╝██║  ██║██║  ██║██║  ██╗    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║{RESET}
{NEON_PINK}  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝{RESET}

{NEON_CYAN}  [██████░░░░░░░░░░░░░░░░░░░░░░░░░░] 18%{RESET}
{NEON_PURPLE}> Initializing core...{RESET}
{NEON_BLUE}> Linking shadow protocols...{RESET}
{NEON_GREEN}> Awakening system...{RESET}
"""

    terminal_size = get_terminal_size()
    centered_text = center_text(text, terminal_size.columns)
    colors = [NEON_PINK, NEON_CYAN, NEON_PURPLE, NEON_GREEN, NEON_BLUE]

    for _ in range(4):
        for color in colors:
            clear()
            print(f"{color}{centered_text}{RESET}")
            time.sleep(0.18)

def run_choice(choice):
    if choice == 0:
        os.system('python ./tools/discord.py')
    elif choice == 1:
        os.system('python ./tools/tool_info.py')
    elif choice == 2:
        os.system('python ./tools/geoip.py')
    elif choice == 3:
        os.system('python ./cyb3rtech.py')
    elif choice == 4:
        os.system('python ./cyb3rtech.py')
    elif choice == 5:
        os.system('python ./tools/phone_number.py')
    elif choice == 6:
        os.system('python ./tools/mail_info.py')
    elif choice == 7:
        os.system('python ./tools/username_tracker.py')
    elif choice == 8:
        os.system('python ./tools/sql_vulnerability.py')
    elif choice == 9:
        os.system('python ./tools/discord_raid.py')
    elif choice == 10:
        os.system('python ./tools/dmall.py')
    elif choice == 11:
        os.system('python ./tools/discord_token_info.py')
    elif choice == 12:
        os.system('python ./tools/discord_token_nuker.py')
    elif choice == 13:
        os.system('python ./tools/discord_token_joiner.py')
    elif choice == 14:
        os.system('python ./tools/discord_token_bruteforce.py')
    elif choice == 15:
        os.system('python ./cyb3rtech.py')
    elif choice == 16:
        os.system('python ./cyb3rtech.py')
    elif choice == 17:
        os.system('python ./tools/discord_nitro_generator.py')
    elif choice == 18:
        os.system('python ./cyb3rtech.py')
    elif choice == 19:
        os.system('python ./tools/web_cloner.py')
    elif choice == 20:
        os.system('python ./nextpage.py')
    else:
        print(f"{NEON_RED}[!] > Invalid choice < [!]{RESET}")
        time.sleep(2)

def main():
    blinking()

    menu = f"""
{NEON_PINK}             ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗{RESET}
{NEON_CYAN}             ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║███████╗{RESET}
{NEON_PURPLE}           ██║  ██║███████║██████╔╝█████╔╝     ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗{RESET}
{NEON_BLUE}             ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║{RESET}
{NEON_GREEN}             ██████╔╝██║  ██║██║  ██║██║  ██╗    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║{RESET}
{NEON_PINK}             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝{RESET}
{NEON_CYAN}                          ░                          ░ ░ {RESET}
{NEON_PURPLE}                                    By Justnutellabrot {RESET}
{NEON_BLUE}                                             ║{RESET}
{NEON_GREEN}                                             ║{RESET}
{NEON_PINK}                                             ║{RESET}
{NEON_CYAN}      ╔══════════════════════════════════════════════════════════════════════════════════╗{RESET}
{NEON_PURPLE}    ║ Dark Nexus | Beta | [0] > Support (discord)                    [ - ] [ □ ] [ X ] ║{RESET}
{NEON_BLUE}      ║══════════════════════════════════════════════════════════════════════════════════║{RESET}
{NEON_GREEN}     ║                                                                                  ║{RESET}
{NEON_PINK}      ║ [1] > Tool Info                 [11] > Discord Token Info                        ║{RESET}
{NEON_CYAN}      ║ [2] > IP Info                   [12] > Discord Token Nuker                       ║{RESET}
{NEON_PURPLE}    ║ [3] > DDOS (#soon)              [13] > Discord Token Joiner                      ║{RESET}
{NEON_BLUE}      ║ [4] > Mass Report (#soon)        [14] > Discord Token BruteForce                 ║{RESET}
{NEON_GREEN}     ║ [5] > Phone Number Lookup        [15] > N/A                                      ║{RESET}
{NEON_PINK}      ║ [6] > Mail Info                  [16] > Discord Token Generator                  ║{RESET}
{NEON_CYAN}      ║ [7] > Username Tracker           [17] > Discord Nitro Generator                  ║{RESET}
{NEON_PURPLE}    ║ [8] > SQL Vulnerability          [18] > Discord Server Info                      ║{RESET}
{NEON_BLUE}      ║ [9] > Discord Raid               [19] > Web Cloner (#soon)                       ║{RESET}
{NEON_GREEN}     ║ [10] > Dmall                     [20] > Next Page (1/2) (#soon)                  ║{RESET}
{NEON_PINK}      ║                                                                                  ║{RESET}
{NEON_CYAN}      ╚══════════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

    while True:
        clear()
        print(menu)
        try:
            choice = int(input(f"{NEON_PINK}Choice >> {RESET}"))
            run_choice(choice)
            time.sleep(1)
        except ValueError:
            print(f"{NEON_RED}[!] > Invalid choice < [!]{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()
