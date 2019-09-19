import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("https://www.baidu.com")
dr.maximize_window()
st = dr.find_element_by_id("kw")
st.send_keys("selenium")
st.send_keys(Keys.BACK_SPACE)
st.send_keys(Keys.SPACE)
st.send_keys("python3")
st.send_keys(Keys.CONTROL,"a")
st.send_keys(Keys.CONTROL,"c")
st.clear()
time.sleep(2)
st.send_keys(Keys.CONTROL,"v")
su = dr.find_element_by_id("su").send_keys(Keys.ENTER)