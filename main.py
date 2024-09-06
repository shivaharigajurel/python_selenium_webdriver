from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

product_url = "https://www.python.org/"
driver.get(product_url)

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# name = driver.find_element(By.ID, "productTitle")

# product_price = f"{price_dollar.text}.{price_cents.text}"
# print(f"The price is ${product_price}")

# print(f"{name.text}")

# driver.find_element()
 

bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


driver.find_element(By.CSS_SELECTOR, )

driver.quit()