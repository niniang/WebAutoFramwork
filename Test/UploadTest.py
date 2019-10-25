from selenium import webdriver
import time

dr = webdriver.Chrome();
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('file:///E:/PycharmProjects/WebAutoFramwork/test.html')
time.sleep(3)
dr.find_element_by_name('pic').send_keys('E:/PycharmProjects/WebAutoFramwork/test.html')
time.sleep(3)
dr.find_element_by_name('submit').click()
