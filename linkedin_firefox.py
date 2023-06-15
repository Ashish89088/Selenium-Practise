from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as Keys

driver = webdriver.Firefox()

driver.get("https://in.linkedin.com/")

username = driver.find_element(by=By.ID, value="session_key")
username.send_keys("ashishsah89088@gmail.com")

password = driver.find_element(by=By.ID, value="session_password")
password.send_keys("Ashish12345")

submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
submit.send_keys(Keys.ENTER)