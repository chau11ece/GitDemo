import collections
import re

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="D:\\WebDriver\\geckodriver.exe")

# driver.get("https://www.familysearch.org/en/")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element_by_css_selector("a[href*='shop'").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

print(len(products))
print("Hello world")
print("Update scripts")


# Done few more steps

def count_email_domain_v1p0():
    with open('emails.text') as f:
        text = f.read()

    domains = re.findall(r'@(.*)$', text, re.MULTILINE)
    mail_values = collections.Counter(domains)
    # Outputs example: Counter({'gmail.com':4, 'yahoo.com':3})
    return mail_values


for product in products:
    prod_name = product.find_element_by_xpath("div/h4/a").text
    # print(prod_name)
    if prod_name == 'Blackberry':
        # Add item into cart
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary'").click()
driver.find_element_by_css_selector("button.btn-success").click()
driver.find_element_by_id("country").send_keys("lan")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Netherlands")))
driver.find_element_by_link_text("Netherlands").click()
driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_css_selector("[type='submit']").click()
success_text = driver.find_element_by_css_selector(".alert-success").text

assert "Success! Thank you!" in success_text

driver.get_screenshot_as_file("screen.png")
