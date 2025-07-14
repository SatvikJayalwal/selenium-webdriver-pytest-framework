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
from pageObjects.login import LoginPage
from pageObjects.ShopPage import ShopPage
from pageObjects.checkout_confirmation import Checkout_Confirmation
import json
from utils.browserutils import BrowserUtils

"""
pytest -m smoke //Tagging
pytest -n 2 //pytest-xdist plugin you need to install to run in parallel
"""

test_data_path="C:\\python_codes\\selenium python\\e2e_TestFramework\\data\\test_e2e_TestFramework.json"
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    
    driver=browserInstance

    #open website
    driver.get("https://rahulshettyacademy.com/loginpagePractise/") #open website url
     
    #calling login page
    login_page=LoginPage(driver)
    print("PAGE TITLE : " , login_page.getTitle())
    login_page.login(test_list_item["userEmail"],test_list_item["userPassword"])

    #calling shop page
    shop_page=ShopPage(driver)
    print("PAGE TITLE : " , shop_page.getTitle())
    shop_page.add_product_to_cart("blackberry")
    shop_page.goToCart()

    #calling checkout_confirmation
    checkout_confirmation=Checkout_Confirmation(driver)
    print("PAGE TITLE : " , checkout_confirmation.getTitle())
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    driver.quit()
