from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Set-up przegladarki
browser = webdriver.Chrome(r"C:\Users\Asus\Desktop\IT\chromedriver_win32 (1)\chromedriver.exe")
browser.get("https://www.google.com/")
browser.maximize_window()

#wyszukiwanie w google
browser.find_element_by_name("q").send_keys("automation practice com")
SearchButton = browser.find_element_by_name("btnK")
SearchButton.click()
browser.find_element_by_class_name("DKV0Md").click()

#sprawdzanie poprawnosci wejscia na strone
title = browser.title
if title != "My Store":
    print("Verification failed - My Store not reached")
else:
    print("Verification successful - My Store has been reached")

#wybierz kategorie i produkt
WomenButton = browser.find_element_by_link_text("Women")
WomenButton.click()
browser.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
browser.find_element_by_link_text("Blouse").click()

#ustaw ilosc sztuk i dodaj do koszyka
browser.execute_script("window.scrollTo(0, 500)")
browser.find_element_by_name("qty").clear()
browser.find_element_by_name("qty").send_keys("99")
browser.find_element_by_name("Submit").click()
browser.find_element_by_class_name("btn-default").click()

#oproznij koszyk
browser.get("http://automationpractice.com/index.php?controller=order")
browser.execute_script("window.scrollTo(0, 500)")
browser.find_element_by_id("2_7_0_0").click()

#asercja - koszyk jest pusty/ order tab
shoppingCart = browser.find_element_by_xpath("//*[contains(text(), 'Your shopping cart is empty.')]")
title = browser.title
assert title == "Order - My Store"
browser.quit()

