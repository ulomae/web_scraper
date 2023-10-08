from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://www.indeed.com/")
driver.maximize_window()
time.sleep(3)


search_job = driver.find_element(By.ID, "text-input-what")
search_place = driver.find_element(By.ID, "text-input-where")

search_job.send_keys(Keys.CONTROL + "a")
search_job.send_keys(Keys.DELETE)

search_place.send_keys(Keys.CONTROL + "a")
search_place.send_keys(Keys.DELETE)

search_job.send_keys("Software Intern")
search_place.send_keys("Irvine, CA")
search_place.send_keys(Keys.RETURN)
time.sleep(2)

date_button = driver.find_element(By.ID, "filter-dateposted")
date_button.click()

date_filter = driver.find_element(By.LINK_TEXT, "Last 24 hours")
date_filter.click()
time.sleep(2)
miles_button = driver.find_element(By.ID, "filter-radius")
miles_button.click()

miles_filter = driver.find_element(By.LINK_TEXT, "Within 25 miles")
miles_filter.click()






