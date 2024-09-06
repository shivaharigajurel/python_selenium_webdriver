from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver  =  webdriver.Chrome(options=chrome_options)

url = "https://www.python.org/"
driver.get(url)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
    
    
event = {}

for n in range(len(event_times)):
    event[n+1] = {
        "time":event_times[n].text,
        "name":events[n].text
    }
    
print(event)