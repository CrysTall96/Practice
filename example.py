from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
# execute the path where you stored your chromedriver
driver = webdriver.Chrome(executable_path='driver/chromedriver')

# Opens the URL to maximize the window
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# defines username, password, and login by id
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login = driver.find_element(By.ID, 'login-button')
# enters user information
username.send_keys('standard_user')
password.send_keys('secret_sauce')
# press login
login.submit()
item_one_ele = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
item_one = item_one_ele.text
print(item_one)
desc_one = driver.find_element(By.CLASS_NAME, 'inventory_item_desc').text
print(desc_one)
price_one = driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
print(price_one)
url_one = driver.current_url
print(url_one)
item_one_ele.click()

item_two = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text
print(item_two)
desc_two = driver.find_element(By.CLASS_NAME, 'inventory_details_desc').text
print(desc_two)
price_two = driver.find_element(By.CLASS_NAME, 'inventory_details_price').text
print(price_two)
url_two = driver.current_url
print(url_two)

#verifies name is same on both pages
assert item_one == item_two
#verifies description is same on both pages
assert desc_one == desc_two
#verifies price is same on both pages
assert price_one == price_two
#verifies urls are not the same on each page
assert url_one != url_two

time.sleep(5)


# verify price of items
# add to cart, then click cart, verify the quantity is 1
# verify description title and price
# click item
# test back to products
