import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import openpyxl
import pytest
from utils.browserutils import BrowserUtils

class LoginPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        
        self.userinput_name=(By.ID,"username")
        self.userinput_password=(By.ID,"password")
        self.userinput_login=(By.ID,"signInBtn")
    
    def login(self,username,password):
        
        #fill login details 
        self.driver.find_element(*self.userinput_name).send_keys(username) # (*) breaks tuple in 2 arguments (By.ID,"username")
        self.driver.find_element(*self.userinput_password).send_keys(password)
        self.driver.find_element(*self.userinput_login).click()
