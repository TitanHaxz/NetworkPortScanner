import socket
import os
from colorama import Fore, Style, init
init()

SERVICES = {
    "RDP":{
        20: "TCP FTP",
        21: "TCP FTP",
        3389: "TCP RDP",
        3306: "TCP MySQL",
    },
    "SSH":{
        20: "TCP FTP",
        21: "TCP FTP",
        21: "TCP SSH",
        3306: "TCP MySQL",
    },
    "cPanel": {
        20: "TCP FTP",
        21: "TCP FTP",
        22: "TCP SSH",
        26: "TCP SMTP",
        53: "TCP DNS",
        53: "UDP DNS",
        80: "TCP HTTP",
        143: "TCP IMAP",
        443: "TCP HTTP",
        443: "UDP HTTP",
        465: "TCP SMTP",
        993: "TCP IMAP",
        2082: "TCP cPanel Lisans",
        2095: "TCP Webmail",
        3306: "TCP MySQL",
    },
    "Fivem": {
        22: "TCP SSH",
        3389: "TCP RDP",
        3306: "TCP MySQL",
        30120: "TCP Server Query",
        40125: "TCP TxAdmin",
    },
    "Minecraft": {
        22: "TCP SSH",
        3389: "TCP RDP",
        3306: "TCP MySQL",
        25565: "Minecraft Server",
    },
    "TeamSpeak3": {
        9987: "UDP Voice",
        30033: "TCP Filetransfer",
        10011: "TCP ServerQuery(raw) (Optional)",
        10022: "TCP ServerQuery(SSH) (Optional)",
    },
    "Metin2": {
        7777: "Metin2 Server",
    },
    "Samp": {
        7777: "SAMP Server",
    },
    "MTA": {
        22003: "MTA Server",
    }
}

def clear_terminal():
    os.system('clear')  # Ubuntu

def check_port(host, port, service_name, port_info):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {port_info}: {Fore.GREEN}{port} {Style.RESET_ALL}")
    else:
        print(f"[{Fore.RED}-{Style.RESET_ALL}] {port_info}: {Fore.RED}{port} {Style.RESET_ALL}")

def choose_service():
    print("Please choose the service you want to check:")
    for idx, service_name in enumerate(SERVICES.keys(), start=1):
        print(f"{Fore.CYAN}{idx}. {Fore.YELLOW}{service_name}{Style.RESET_ALL}")

    choice_idx = int(input("Your choice (Enter a number from 1 to {}): ".format(len(SERVICES))))

    if 1 <= choice_idx <= len(SERVICES):
        service_name = list(SERVICES.keys())[choice_idx - 1]
        return service_name
    else:
        print("Invalid choice. Exiting the program.")
        exit()

def main():
    while True:
        clear_terminal()

        ip_or_domain = input("Please enter an IP or domain: ")

        if ip_or_domain.startswith(('http://', 'https://')):
            ip_or_domain = ip_or_domain.split('//')[1]

        service_name = choose_service()

        print(f"\n{Fore.YELLOW}[+] {service_name} Port Scan is Starting...{Style.RESET_ALL}")

        if service_name in SERVICES:
            for port, port_info in SERVICES[service_name].items():
                check_port(ip_or_domain, port, service_name, port_info)

            user_input = input("\nDo you want to check another service? (y/n): ").lower()
            if user_input != 'y':
                exit()
        else:
            print("Undefined service. Exiting the program.")
            break

if __name__ == "__main__":
    main()
