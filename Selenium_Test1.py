from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Set-up przegladarki
browser = webdriver.Chrome(r"C:\Users\Asus\Desktop\IT\chromedriver_win32 (1)\chromedriver.exe")
browser.get("https://www.google.com/")
browser.maximize_window()

#wyszukiwanie w google
browser.find_element_by_name("q").send_keys("automation practice com")
SearchButton = browser.find_element_by_name("btnK")
SearchButton.click()

#
browser.find_element_by_class_name("DKV0Md").click()
title = browser.title
print(title)
assert "My Store" == title

