from time import ctime
from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(5)

try:
    dr.get("https://www.baidu.com")
    print(ctime())
    tr = dr.find_element_by_id("kw123")
except BaseException as f:
    print(f)
    print(ctime())
finally:
    dr.close()