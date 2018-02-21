
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


ff = webdriver.Chrome()
ff.get("https://www.instagram.com/?hl=en")
# ff.save_screenshot('pics/screenie.png')
# loginButton = ff.find_element_by_class_name('_g9ean').a
# loginButton.send_keys(Keys.RETURN)

#element.send_keys('hossein')

#element.send_keys(Keys.RETURN)
#assert "No results found." not in ff.page_source
#ff.close()

element = ff.find_element_by_class_name('_g9ean')
# print(element)
element = element.find_element_by_xpath('a')
element.click()
userName = ff.find_element_by_name('username')
userName.send_keys('hossein__t_k')
password = ff.find_element_by_name('password')















password.send_keys('5260145143ho')
button = ff.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[1]/div/form/span/button')
#class_name = button.get_attribute('class')
# button.find_element_by_xpath('button')
button.click()




