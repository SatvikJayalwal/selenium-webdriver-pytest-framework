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


class BrowserUtils:

    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        return self.driver.title 
    