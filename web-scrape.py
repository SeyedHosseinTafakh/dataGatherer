from asyncio import wait_for
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




ch = webdriver.Chrome()
ch.get("https://www.instagram.com/?hl=en")
element = ch.find_element_by_class_name('_g9ean')
element = element.find_element_by_xpath('a')
element.click()
userNameInput = ch.find_element_by_name('username')
userNameInput.send_keys('shandool_paroon4')
password = ch.find_element_by_name('password')


password.send_keys('123456789h')

button = ch.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[1]/div/form/span/button')
button.click()

element = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')))
print(element)
userName = 'hossein__t_k'
ch.get("https://www.instagram.com/" + userName + "/")
followersButton = ch.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a')
followersNumber = ch.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a/span')

followersNumber  = followersNumber.get_attribute('title')
followersButton.click()

element = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]')))
element = element.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/ul/div/li[1]/div/div[1]/div/div[1]/a')
print(element.get_attribute('text'))

ch.execute_script("window.scrollTo(0, document.body.scrollHeight);")



