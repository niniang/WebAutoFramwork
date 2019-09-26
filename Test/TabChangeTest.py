from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.maximize_window()
win_handle = dr.current_window_handle
print(win_handle)
js = 'window.open("http://news.baidu.com")'
dr.execute_script(js)
handles = dr.window_handles
time.sleep(5)

for i in handles:
    if i == win_handle:
        dr.switch_to.window(i)

dr.switch_to.window(win_handle)
tr = dr.find_element_by_id('kw')
tr.send_keys('test')
time.sleep(5)

for i in handles:
    if i != win_handle:
        dr.switch_to.window(i)
ww = dr.find_element_by_id('ww')
ww.send_keys('test')
time.sleep(5)


dr.quit()