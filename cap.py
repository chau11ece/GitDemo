from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path="D:\\WebDriver\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(3)

# driver.find_element_by_css_selector("input.search-keyboard").send_keys("ber")
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# //div[@class='product-action']/button/parent::div/parent::div/h4

prod_list_adding = []
prod_list_added = []

for button in buttons:
    prod_name = button.find_element_by_xpath("parent::div/parent::div/h4")
    # print(prod_name.text)
    prod_list_adding.append(prod_name.text)
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[contains(.,'PROCEED TO CHECKOUT')]").click()

driver.implicitly_wait(10)

veggies = driver.find_elements_by_css_selector("p.product-name")
prod_list_added = [veg.text for veg in veggies if veg.text.strip()]

print(prod_list_adding)
print(prod_list_added)

assert prod_list_adding == prod_list_added

total_amount = driver.find_element_by_css_selector(".totAmt").text

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discount_amount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discount_amount) < int(total_amount)

print(discount_amount, total_amount)
print(driver.find_element_by_css_selector(".promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum_price = 0

for amount in amounts:
    sum_price += int(amount.text)

print(sum_price)

assert int(sum_price) == int(total_amount)

# test updating codes
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")

for city in cities:
    print(city.text)


for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

