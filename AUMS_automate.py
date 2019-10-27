import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/home/sreejith/Downloads/chrome-driver/chromedriver")

username = sys.argv[1]
password = sys.argv[2]
start = 61
browser.maximize_window()

browser.get('https://aums-students-am.amrita.edu:8443/cas/login?service=https%3A%2F%2Faums-students-am.amrita.edu'
            '%3A8443%2Faums%2FJsp%2FCore_Common%2Findex.jsp')
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
    strings = 'https://aums-apps-5.amrita.edu:8443/portal/tool/b610fc22-f1be-4655-b1ab-5bfcc1d97b32/take_eval' \
              '?evaluationId=64&reOpening=false&evalGroupId=adhoc-group%3A222' + str(start)
    browser.get(strings)

    actions = ActionChains(browser)
    for _ in range(20):
        actions.send_keys(Keys.SPACE)
        actions.perform()
        actions.send_keys(Keys.TAB)
        actions.perform()
