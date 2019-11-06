from selenium import webdriver
from PageObject.BaiduPage import baidu
import unittest

class BaiduSearch(unittest.TestCase):

    def baiduPageTest(self):
        dr = webdriver.Chrome()
        dr.get('https://www.baidu.com')
        bai = baidu(dr)
        bai.kw_send('selenium')
        bai.su_click()

if __name__ == '__main__':
    unittest.main()