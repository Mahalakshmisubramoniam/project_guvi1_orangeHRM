
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data import testdata
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class Test_Orange:
    url = "https://opensource-demo.orangehrmlive.com"

    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()


    # python code to automate login
    def test_login(self, booting_function):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            time.sleep(5)
            self.driver.find_element(by=By.NAME, value=testdata.test_Orange_Selectors.input_box_username).send_keys(testdata.test_Orange_Data.username)
            self.driver.find_element(by=By.NAME, value=testdata.test_Orange_Selectors.input_box_password).send_keys(testdata.test_Orange_Data.password)
            self.driver.find_element(by=By.XPATH, value=testdata.test_Orange_Selectors.login_xpath).click()
            assert self.driver.title == 'OrangeHRM'
            print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=testdata.test_Orange_Data.username, password=testdata.test_Orange_Data.password))
        except:
            print("error:try login again!")


    # python code to automate employee detail edit
    def test_edit_employee_list(self,booting_function):
        Test_Orange.test_login(self, booting_function)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=testdata.test_Orange_edit_selector.pim_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=testdata.test_Orange_edit_selector.edit_icon_xpath).click()
        self.driver.find_element(by=By.NAME, value=testdata.test_Orange_edit_selector.name).send_keys(testdata.test_orange_edit_data.input_name)
        self.driver.find_element(by=By.NAME, value=testdata.test_Orange_edit_selector.middlename).send_keys(testdata.test_orange_edit_data.input_middlename)
        assert self.driver.title == 'OrangeHRM'


    # python code to automate delete action
    def test_delete_employee(self, booting_function):
        Test_Orange.test_login(self, booting_function)
        self.driver.find_element(by=By.XPATH, value=testdata.test_Orange_delete.delete_xpath).click()
        self.driver.find_element(by=By.XPATH, value=testdata.test_Orange_delete.delete_xpath1).click()
        assert self.driver.title == 'OrangeHRM'
        print("employee details deleted")
