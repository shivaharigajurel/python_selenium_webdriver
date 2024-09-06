from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

page_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(page_url)

# article_count = driver.find_element(By.CSS_SELECTOR, 
# value="#articlecount a")
# article_count.click()
# print(article_count.text)


# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")

# all_portals.click()


search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "search"))
)
search.send_keys("Python", Keys.ENTER)
