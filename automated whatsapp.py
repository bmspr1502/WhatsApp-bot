from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\Users\Home\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)


names = [""]#add the person's name whom who want to reply automatically
            #add as many persons you want   

while True:
    for name in names:
        person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        person.click()

        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got]
        if msg[-1] == "Hi":
            reply = driver.find_elements_by_class_name("_2S1VP")
            reply[1].clear()
            reply[1].send_keys("hi\n tell me")
            reply[1].send_keys(Keys.RETURN)
 
