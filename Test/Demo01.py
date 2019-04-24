from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.baidu.com')
time.sleep(3)

#test = dr.find_element_by_name('wd')
#test = dr.find_element_by_id('kw')
#test = dr.find_element_by_class_name('s_ipt')
test = dr.find_element_by_xpath('//*[@id="kw"]')
#test = dr.find_elements_by_css_selector('#kw')
test.send_keys('test')

#test = dr.find_element_by_link_text('新闻')
#test = dr.find_element_by_partial_link_text('hao')
#test.click()

time.sleep(3)
#dr.close()