from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

options = ChromeOptions()
options.add_experimental_option("detach", True)

options.page_load_strategy = 'normal'
service = ChromeService()
driver = webdriver.Chrome(options=options,service=service)
# driver = webdriver.Chrome(options=options)



# driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
assert title == "Web form"

driver.implicitly_wait(5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
value = message.text
assert value == "Received!"

driver.quit()