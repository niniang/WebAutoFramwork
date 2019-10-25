from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://www.baidu.com/')

dr.add_cookie({'name':'BDUSS','value':'UptdVZOVWI1REYyR2lsSkRYRWY3Z1diMXRFT0FyVUNsUjJaYWJUbjN3UVh2YXRkSVFBQUFBJCQAAAAAAAAAAAEAAABcsk40ztK1xElExN~E37C6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcwhF0XMIRdV'})
dr.get('https://www.baidu.com/')