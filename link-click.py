import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/xampp/htdocs/web/python-programs/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.guru99.com/selenium-python.html');
time.sleep(4) # Let the user actually see something!
search_box = driver.find_element_by_link_text('Python')
search_box.click()

time.sleep(5) # Let the user actually see something!
driver.quit()