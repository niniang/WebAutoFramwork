from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.maximize_window()
dr.find_element_by_id('kw').send_keys('test')
dr.find_element_by_id('su').click()
time.sleep(3)
js = "window.scrollTo(0,0)"
js01 = "window.scrollTo(0,document.body.scrollHeight)"
dr.execute_script(js01)
time.sleep(3)
dr.execute_script(js)
#dr.find_element_by_link_text('百度首页').click()
st = dr.find_element_by_id("kw")
st.clear()
time.sleep(3)
st.send_keys("yuhan")
time.sleep(3)
dr.find_element_by_id('su').click()