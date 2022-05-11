from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# i did: python -m pip install selenium

# opening browser on http://192.168.0.1/
driver = webdriver.Chrome('./chromedriver')
driver.get('http://192.168.0.1/')
driver.implicitly_wait(2)  # seconds

# registering and inserting login fields
loginUser = driver.find_element(by=By.XPATH, value='//*[@id="userName"]')
loginPW = driver.find_element(by=By.XPATH, value='//*[@id="pcPassword"]')
loginButton = driver.find_element(by=By.XPATH, value='//*[@id="loginBtn"]')
driver.implicitly_wait(2)  # seconds
loginUser.send_keys('admin')
loginPW.send_keys('admin')
loginButton.click()

# waiting till element appears in the page
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# try:
#     time.sleep(10)
#     window_after = driver.window_handles[1]
#     driver.switch_to.window(window_after)
# finally:
#     print('didnt catch the new window_handles')

wireless = driver.find_element(by=By.ID, value='a9')
MACfiltering = driver.find_element(by=By.ID, value='a12')
try:
    filterButton = driver.find_element(by=By.ID, value='Enfilter')
    filterButton.click()
except []:
    print('no Enfilter button')

try:
    filterButton = driver.find_element(by=By.ID, value='Disfilter')
    filterButton.click()
except []:
    print('no Disfilter button')
    driver.quit()

#------------------------------
# try:
#     wireless = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "a9"))
#     )
#     wireless.click()
# finally:
#     print('no wireless section')
#
# try:
#     MACfiltering = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, 'a12'))
#     )
#     MACfiltering.click()
# finally:
#     print('no MACfiltering sub-section')
#
# try:
#     filterButton = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.NAME, 'Enfilter'))
#     )
#     filterButton.click()
# finally:
#     print('no Enfilter button')
#
# try:
#     filterButton = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'Disfilter'))
#     )
#     filterButton.click()
# except:
#     print('no Disfilter button')
#     driver.quit()
# traversing into the filter page
# driver.implicitly_wait(2) # seconds
# wireless = driver.find_elements_by_xpath('//*[@id="a9"]')
# wireless.click()
# driver.implicitly_wait(2) # seconds
# MACfiltering = driver.find_element_by_xpath('//*[@id="a12"]/span')
# MACfiltering.click()

# pressing the enab'e/disable filter button
# filterButton = driver.find_elements_by_xpath('//*[@id="autoWidth"]/tbody/tr[3]/td[2]/input[2]')
# filterButton.click()

# logging out and closing window
# driver.implicitly_wait(5) # seconds
# logoutButton = driver.find_element_by_xpath('//*[@id="a61"]')
# logoutButton.click()

# driver.quit()
