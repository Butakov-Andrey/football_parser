import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from football_events import main

events = main()
keys = list(events.keys())
event = events[keys[0]]

browser = webdriver.Chrome()
browser.get('https://www.fonbet.ru/')

time.sleep(3)

search_button = browser.find_element(By.CLASS_NAME, 'search__link')
ActionChains(browser).click(search_button).perform()

search = browser.find_element(By.CLASS_NAME, 'search__input--DF661')
search.send_keys(event)
search.send_keys(Keys.RETURN)

time.sleep(3)

event_button = browser.find_element(By.CLASS_NAME, 'search-result__event-name--3Qfnn')
ActionChains(browser).click(event_button).perform()

print(event)

time.sleep(99999)
