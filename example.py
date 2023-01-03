from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
# execute the path where you stored your chromedriver
driver = webdriver.Chrome(executable_path='driver/chromedriver')

# Opens the URL
driver.get("https://www.saucedemo.com/")

# defines which item is which
elements = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
item_zero = elements[0]
item_one = elements[1]
item_two = elements[2]

# defines username, password, and login by id
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login = driver.find_element(By.ID, 'login-button')

# enters user information
username.send_keys('standard_user')
password.send_keys('secret_sauce')

time.sleep(3)

# press login
login.submit()

# gathering information
item_zero_ele = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
item_zero = item_zero_ele.text
print(item_zero)
desc_zero = driver.find_element(By.CLASS_NAME, 'inventory_item_desc').text
print(desc_zero)
price_zero = driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
print(price_zero)
url_zero = driver.current_url
print(url_zero)
item_zero_ele.click()

# gathering information
# item one name
item_one = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text
print(item_one)
# description of item one
desc_one = driver.find_element(By.CLASS_NAME, 'inventory_details_desc').text
print(desc_one)
# price of item one
price_one = driver.find_element(By.CLASS_NAME, 'inventory_details_price').text
print(price_one)
# checking the url
url_one = driver.current_url
print(url_one)

# verifies name is same on both pages
assert item_zero == item_one
# verifies description is same on both pages
assert desc_zero == desc_one
# verifies price is same on both pages
assert price_zero == price_one
# verifies urls are not the same on each page
assert url_zero != url_one

time.sleep(3)

# defines what back to the home page button is
back_button = driver.find_element(By.ID, 'back-to-products')
# clicks back button
back_button.click()

time.sleep(3)

# defines item one


# verify price of items
# add to cart, then click cart, verify the quantity is 1
# verify description title and price
# click item
# test back to products
