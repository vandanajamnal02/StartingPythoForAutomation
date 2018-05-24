import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver

self.driver = webdriver.Firefox()
self.driver.get("http://www.python.org")
