from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('file:///E:/PycharmProjects/WebAutoFramwork/test.html')
dr.switch_to.frame('if')
st = dr.find_element_by_id('kw')
st.send_keys('test')