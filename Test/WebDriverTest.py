from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("https://www.baidu.com")#打开百度
tr = dr.title
print(tr)
wait = WebDriverWait(dr,10)#实例化显示等待，10s
s = wait.until(expected_conditions.title_contains('百度'),'出错了')
print(s)



