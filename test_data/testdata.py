# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class test_Orange_Data:
    username = "Admin"
    password = "admin123$"

# Python Class for Selenium Selectors
class test_Orange_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

class test_Orange_edit_selector:
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    edit_icon_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/button[2]'
    name = 'firstName'
    middlename = 'middleName'

class test_orange_edit_data:
    input_name = 'mahalakshmi'
    input_middlename = 'sivasubramoniam'

class test_Orange_delete:
    delete_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/button[1]'
    delete_xpath1 = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'