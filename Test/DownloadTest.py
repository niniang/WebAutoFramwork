from selenium import webdriver
import os

option = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups':0,'download.default_directory':'E:\\'}
option.add_experimental_option('prefs',prefs)

dr = webdriver.Chrome(chrome_options=option)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://www.seleniumhq.org/download/')
dr.find_element_by_xpath('//*[@id="mainContent"]/table[1]/tbody/tr[1]/td[4]/a').click()