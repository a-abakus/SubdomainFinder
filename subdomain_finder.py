import sys
import dns.resolver
from pyfiglet import figlet_format


def dns_resolver(subdomains, domain):
    for sub in subdomains:
        try:
            resolver = dns.resolver.resolve(f"{sub}.{domain}", "A")
            if resolver:
                print(f"Found {sub}.{sys.argv[1]}")
        except dns.resolver.NXDOMAIN:
            pass
        except KeyboardInterrupt:
            return


def main():
    if len(sys.argv) < 3:
        print("Usage: python3", sys.argv[0], "<example.com> <wordlist_path>")
        return

    domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    try:
        with open(wordlist_path) as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print("Wordlist Not Found!")
        return

    dns_resolver(subdomains, domain)


if __name__ == "__main__":
    print(figlet_format("Subdomain Finder", font="small"))
    main()
