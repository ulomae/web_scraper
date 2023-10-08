from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.indeed.com/")
#driver.maximize_window()
time.sleep(5)

search_job = driver.find_element("id", "text-input-what")
search_place = driver.find_element("id", "text-input-where")
search_place.send_keys(Keys.CONTROL + "a")
search_place.send_keys(Keys.DELETE)
search_job.send_keys("Software Intern")
search_place.send_keys("Irvine, CA")
search_place.send_keys(Keys.RETURN)
#search = driver.find_element("className", "yosegi-InlineWhatWhere-primaryButton").click()



