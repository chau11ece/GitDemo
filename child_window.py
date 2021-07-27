from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path="D:\\WebDriver\\geckodriver.exe")

driver.get("http://the-internet.herokuapp.com/windows")
driver.implicitly_wait(3)

driver.find_element_by_link_text("Click Here").click()

parent_window = driver.window_handles[0]
child_window = driver.window_handles[1]

# ("parentid", "childid")
driver.switch_to.window(child_window)
text_ele = driver.find_element_by_tag_name("h3")
print(text_ele.text)
driver.close()
driver.switch_to.window(parent_window)
print(driver.find_element_by_tag_name("h3").text)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
