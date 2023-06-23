import time 

from anticaptchaofficial.recaptchav2proxyless import *

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from const import token_api


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URI = 'https://www.google.com/recaptcha/api2/demo'

SITEKEY_XPATH = '//*[@id="recaptcha-demo"]'

source_page = driver.get(URI)
time.sleep(5)

sitekey = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, SITEKEY_XPATH))
).get_attribute('outerHTML')

site_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(token_api)
solver.set_website_url(URI)
solver.set_website_key(site_clean)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print('g_response'+g_response)
else:
    print('Error' + solver.error_code)


driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-demo-submit"]'))
).click()

time.sleep(45)






