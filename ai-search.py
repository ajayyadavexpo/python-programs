import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# web scraping
import requests

path = 'C:/xampp/htdocs/web/python-programs/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 1}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


def search_text(text):
	url = "https://www.google.com/search?q="
	driver.get(url+text.replace(" ","+"));
	time.sleep(4) # Let the user actually see something!
	class_name = driver.find_element_by_class_name('kno-rdesc')
	print(class_name)





# driver.get(url);
# time.sleep(4) # Let the user actually see something!
# search_box = driver.find_element_by_name("searchKeyword")
# search_box.send_keys("Technology")
# button = driver.find_element_by_class_name('_2VoZY')
# button.click()
# time.sleep(2)
# image = driver.find_element_by_class_name('_2zEKz')
# image.click()
# time.sleep(2)


# download_link = driver.find_element_by_class_name('_13Q-')
# download_link.click()

search_text('what is laravel')
time.sleep(5) # Let the user actually see something!
driver.quit()