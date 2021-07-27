from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


driver = webdriver.Firefox(executable_path="D:\\WebDriver\\geckodriver.exe")

# driver.get("https://www.familysearch.org/en/")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.implicitly_wait(3)
# ActionChains

# search_ele = driver.find_element_by_id("search")
# action = ActionChains(driver)
# action.move_to_element(search_ele).perform()
# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

dbl_click = driver.find_element_by_id("double-click")
action = ActionChains(driver)
action.double_click(dbl_click).perform()

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present)
    alert = driver.switch_to.alert
    assert "You double clicked me!!!, You got to be kidding me" == alert.text
    alert.accept()
except:
    print("Pls double-click quickly!")
finally:
    print("PASS!")

assert expression
assert not expression

print(driver.find_element_by_name("name").get_attribute("value"))
driver.execute_script('return document.getElementsByTagName("name")[0].value')
