#coding=utf-8
import selenium

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_key("Selenium2")
dirver.find_element_by_id("su").click()
driver.quit
