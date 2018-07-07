'''
WANT TO MAKE:
Image Distorter
Voice Distorter
Text to slan converter

'''

# http://www.robertecker.com/hp/research/leet-converter.php


from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from fblogin import username,password #shifted to seperate file

# from pynput.keyboard import Key, Controller

# import keyboard

# keyboard = Controller()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

leet_converter = 'http://www.robertecker.com/hp/research/leet-converter.php'
driver.get(leet_converter)
inputbox = driver.find_element_by_name('textbox_input')

user_input = input('Enter text to Convert:')
inputbox.send_keys(user_input)

encode_button = driver.find_element_by_name('encode')
encode_button.click()

outputbox = driver.find_element_by_name('user_textbox_output')
print(outputbox.text)

