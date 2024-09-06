from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)


first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

button= driver.find_element(By.CLASS_NAME, value="btn-primary")


first_name.send_keys("Shivahari")
last_name.send_keys("Gajurel")
email.send_keys("hdhf@jdjf.com")

button.click()