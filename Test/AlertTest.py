from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://www.baidu.com')

sz = dr.find_element_by_link_text('设置')
ActionChains(dr).move_to_element(sz).perform()

dr.find_element_by_link_text('搜索设置').click()
sst = dr.find_element_by_class_name('prefpanelgo')
sst.send_keys(Keys.ENTER)

time.sleep(5)
#dr.switch_to_alert().send_keys(Keys.ENTER)
dr.switch_to_alert().accept()

