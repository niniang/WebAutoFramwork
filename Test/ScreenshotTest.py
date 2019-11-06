from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('su').click()
time.sleep(3)
dr.get_screenshot_as_file('D:\\test.png')#jpg不行