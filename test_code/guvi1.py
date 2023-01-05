from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data import testdata
from selenium.webdriver.common.action_chains import ActionChains

class orange:

     driver = webdriver.Chrome()
     def test_login(self):
         driver.get("https://opensource-demo.orangehrmlive.com")

