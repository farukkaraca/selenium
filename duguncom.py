from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def forlogin():
    browser=webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://www.dugun.com")
    time.sleep(5)
    login=browser.find_element_by_xpath('''//*[@id="userModalButton"]/div/div[1]/a''')
    login.click()
    time.sleep(2)
    mail=browser.find_element_by_name("email")
    mail.send_keys("youremail")
    time.sleep(1)
    password=browser.find_element_by_name("password")
    password.send_keys("yourpassword")
    time.sleep(1)
    login1=browser.find_element_by_xpath('''//*[@id="userModal"]/div[2]/div/div/div/div[2]/div[1]/div/form/div[3]/div/div/button''')
    login1.click()
def resetpassword():
    browser=webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://www.dugun.com")
    time.sleep(5)
    login=browser.find_element_by_xpath('''//*[@id="userModalButton"]/div/div[1]/a''')
    login.click()
    time.sleep(1)
    forgotmypassword=browser.find_element_by_xpath('''//*[@id="userModal"]/div[2]/div/div/div/div[2]/div[1]/div/form/div[2]/div/p/a''')
    forgotmypassword.click()
    mail1=browser.find_element_by_name("email")
    mail1.send_keys("youremail")
    wantnewpassword=browser.find_element_by_xpath('''//*[@id="userModal"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/form/div[2]/div/button''')                                               
    wantnewpassword.click()

#forlogin()
#resetpassword()

