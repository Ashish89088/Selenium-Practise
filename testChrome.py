from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys as K


options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

text_box = driver.find_element(by=By.ID, value="APjFqb")
text_box.send_keys("Selenium")
text_box.send_keys(Keys.ENTER)


# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# submit_button.click()