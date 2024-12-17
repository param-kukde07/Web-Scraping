import os 
import time 
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# driver = webdriver.Chrome(service=Service("/home/vedant/Downloads/chromedriver-linux64/chromedriver"))
driver = webdriver.Chrome(options= options)
driver.get('https://freesearchigrservice.maharashtra.gov.in/')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/center/form/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[2]'))
).click()


dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ddlFromYear1"]'))
)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('2023')


dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ddlDistrict1"]'))
)
dropdown = Select(dropdown_element)
dropdown.select_by_value('1')


dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ddltahsil"]'))
)
dropdown = Select(dropdown_element)
dropdown.select_by_value('7')

time.sleep(5)

captcha_element = driver.find_element(By.XPATH, '//*[@id="imgCaptcha_new"]')
captcha_element.screenshot('captcha.png')

captcha_text = pytesseract.image_to_string(Image.open('captcha.png')).strip()
print(f"Extracted CAPTCHA text: {captcha_text}")
captcha_input = driver.find_element(By.XPATH, '//*[@id="txtImg1"]')
captcha_input.click()
for char in captcha_text:
    captcha_input.send_keys(char)
    time.sleep(0.2)
time.sleep(10)

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSearch_RestMaha"]'))
)
submit_button.click()
time.sleep(10)
driver.quit()