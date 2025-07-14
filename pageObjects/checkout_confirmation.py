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

class Checkout_Confirmation(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.checkout_button=(By.XPATH, "//button[@class='btn btn-success']")
        self.country_input=(By.ID,"country")
        self.country_option=(By.LINK_TEXT,"India")
        self.checkbox=(By.XPATH, "//label[@for='checkbox2']")
        self.submit_button=(By.XPATH,"//input[@class='btn btn-success btn-lg']")
        self.success_message=(By.CLASS_NAME,"alert-success")


    def checkout(self):

        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self,country_name):        

        #fill ind and selecct india 
        self.driver.find_element(*self.country_input).send_keys(country_name) #type ind         
        
        #click India from drop down 
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.country_option)).click()
        
        #click the tems and condition checkbox
        self.driver.find_element(*self.checkbox).click()
        #click purchase button 
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):

        success_msg=self.driver.find_element(*self.success_message).text #read and store success msg in success_msg
        assert "Success! Thank you!" in success_msg #check if success_msg is correct and through assertion error if not 
        print(success_msg)


