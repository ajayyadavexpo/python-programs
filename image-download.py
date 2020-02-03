import time
from selenium import webdriver

driver = webdriver.Chrome('C:/xampp/htdocs/web/python-programs/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.pexels.com/search/free%20download/');
time.sleep(4) # Let the user actually see something!
search_box = driver.find_elements_by_css_selector('js-photo-link')
search_box.click()

time.sleep(5) # Let the user actually see something!
driver.quit()