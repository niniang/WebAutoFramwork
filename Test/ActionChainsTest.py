from selenium import webdriver
from selenium.webdriver import ActionChains

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
xw = dr.find_element_by_link_text("新闻")
#ActionChains(dr).context_click(xw).perform()
#xw.click()

sz = dr.find_element_by_link_text("设置")
#ActionChains(dr).move_to_element(sz).perform()

ssl = dr.find_element_by_xpath('//*[@id="kw"]')
ActionChains(dr).drag_and_drop(sz,ssl).perform()
