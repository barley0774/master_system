# from selenium import webdriver
# from time import sleep
# # import chromedriver_binary
# import os

# PATH = os.getcwd()
# print(PATH)
# DRIVER = webdriver.Chrome(PATH +"/chromedriver_linux64/chromedriver")

# def example_auto_box_login():
#     DRIVER.get('https://account.box.com/login')
#     login = DRIVER.find_element_by_name("login")
#     login.clear()
#     login.send_keys("sato0415e@gmail.com")
#     login.submit()

#     password = DRIVER.find_element_by_name("password")
#     password.clear()
#     password.send_keys("iKXB8HWe2")
#     password.submit()

# def auto_box_login(userid, password):
#     DRIVER.get('https://account.box.com/login')
#     login = DRIVER.find_element_by_name("login")
#     login.clear()
#     login.send_keys(userid)
#     login.submit()

#     password = DRIVER.find_element_by_name("password")
#     password.clear()
#     password.send_keys(password)
#     password.submit()