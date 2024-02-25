"""
First install chrome driver or any other browser before running this script

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service #You can choose any browser which is compatible

SITE_LINK ="LINK OF THE SITE"
PATH="PATH OF THE CHROME DRIVER EXE FILE"

#Defining
driver =webdriver.Chrome(service=Service(executable_path=PATH))

#intializing
driver.get(SITE_LINK)

