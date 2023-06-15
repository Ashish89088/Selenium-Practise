from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys as Keys

# PROXY = "http://127.0.0.1:5000"
# PROXY = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
# PROXY = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

options = ChromeOptions()
options.add_experimental_option("detach", True)

# options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(options=options)

driver.get("https://in.linkedin.com/")
# driver.fullscreen_window()

username = driver.find_element(by=By.ID, value="session_key")
username.send_keys("ashishsah89088@gmail.com")

password = driver.find_element(by=By.ID, value="session_password")
password.send_keys("Ashish12345")

submit = driver.find_element(by=By.XPATH, value="//button[normalize-space()='Sign in']")
submit.send_keys(Keys.ENTER)

driver.implicitly_wait(5)

search = driver.find_element(by=By.XPATH, value="//input[@placeholder='Search']")
search.send_keys("machine learning")
driver.implicitly_wait(5)

search.send_keys(Keys.ENTER)

driver.implicitly_wait(5)
people = driver.find_element(by=By.XPATH, value="//button[@aria-pressed='false'][normalize-space()='People']")
people.click()

driver.implicitly_wait(5)
# location = driver.find_element(by=By.XPATH, value="//button[normalize-space()='Locations']")
# location.click()

location_search = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Locations filter. Clicking this button displays all Locations filter options.']")
location_search.click()

# location_input = driver.find_element(by=By.CSS_SELECTOR, value="input[placeholder='Add a location']").send_keys("")
location_check_box = driver.find_element(by=By.XPATH, value="//label[contains(@for,'geoUrn-102713980')]").click()

show_result = driver.find_element(by=By.XPATH, value="//button[@id='ember724']//span[@class='artdeco-button__text'][normalize-space()='Show results']")
show_result.click()
