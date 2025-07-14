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

class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.shop_link=(By.XPATH,"//a[@href='/angularpractice/shop']")
        self.product_cards=(By.XPATH,"//div[@class='card h-100']")
        self.checkout_button=(By.XPATH,"//a[contains(text(),'Checkout')]")

    def add_product_to_cart(self,product_name):
        #click shop
        self.driver.find_element(*self.shop_link).click() #click shop

        #iterate and find blackberry
        products=self.driver.find_elements(*self.product_cards)#find blackberry from multiple products 

        for product in products:
            product_name=product.find_element(By.XPATH,".//h4/a").text

            if product_name.strip().lower()==product_name: #strip() remove space from front/end #lo~wer() lower case
                product.find_element(By.XPATH,".//button").click()  


    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()