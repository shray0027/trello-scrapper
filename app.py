from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from time import sleep

class trello:
    def __init__(self):
         #this chrome driver location is for MAC OS users .
         self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    def process(self):
         driver = self.driver
         try:
            driver.get("enter-your-trello-board-link")
         except:
             driver.close()
    def login(self):
         driver = self.driver
         try:
            sleep(10)
            driver.find_element_by_xpath('// *[ @ id = "surface"] / div[1] / div / div / div[2] / a[2]').click()
            sleep(3)
            email=driver.find_element_by_xpath('//*[@id="user"]')
            email.send_keys("enter-your-email-id")
            sleep(1)
            email.send_keys(Keys.ENTER)
            sleep(6)
            password=driver.find_element_by_class_name('Input__InputElement-sc-1o6bj35-0')
            sleep(1)
            password.send_keys('enter-your-trello-id')
            sleep(1)
            password.send_keys(Keys.ENTER)
            sleep(6)
         except:
            driver.close()

    def makelist(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('// *[ @ id = "board"] / div / form / a / span').click()
            sleep(1)
            input = driver.find_element_by_xpath('// *[ @ id = "board"] / div / form / input')
            input.send_keys('day 1')
            sleep(1)
            input.send_keys(Keys.ENTER)
            for i in range(2, 101):
                input = driver.find_element_by_class_name('list-name-input')
                input.send_keys('day ' + str(i))
                sleep(1)
                input.send_keys(Keys.ENTER)
                sleep(2)
        except:
            driver.close()

t=trello()
t.process()
t.login()
t.makelist()