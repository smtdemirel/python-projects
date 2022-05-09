from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")   
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        time.sleep(2)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def tikla(self):
        giris = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        giris.click()
        giris = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        giris.click()

instagram = Instagram(username,password)
instagram.signIn()
time.sleep(3)
instagram.tikla()   
time.sleep(10)  