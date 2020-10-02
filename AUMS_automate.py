import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/home/sreejith/Downloads/chrome-driver/chromedriver")

username = sys.argv[1]
password = sys.argv[2]
start = 61
browser.maximize_window()

browser.get('AUMS_URL_OF_LOGIN_PAGE')
a = browser.find_element_by_xpath("//input[@id ='username']")
a.send_keys(username)

a = browser.find_element_by_xpath("//input[@id ='password']")
a.send_keys(password)

browser.find_element_by_xpath("//input[@name ='submit']").click()
a = browser.find_element_by_xpath("//input[@id ='username']")
a.send_keys(username)

a = browser.find_element_by_xpath("//input[@id ='password']")
a.send_keys(password)

browser.find_element_by_xpath("//input[@name ='submit']").click()
for i in range(11):
    start = start + 1
    #The below url is unique for each user
    f_url = 'AUMS_URL_TILL_LAST_NO' + str(start)
    browser.get(f_url)

    actions = ActionChains(browser)
    for _ in range(20):
        actions.send_keys(Keys.SPACE)
        actions.perform()
        actions.send_keys(Keys.TAB)
        actions.perform()
