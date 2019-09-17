from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

print('FB LOGIN BOT:')
email_string = input('Write down your email:')
pass_string = input('Write down your password:')
# Open Chrome and load the FB login page
driver = webdriver.Chrome("./chromedriver")
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
# Find the email form input
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(email_string)
print("Email entered...")
# Find the password form input
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(pass_string)
print("Password entered...")
# Click the log in button
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("Logued in into FB")

