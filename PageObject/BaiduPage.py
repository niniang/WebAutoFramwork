from Framework.Base_page import BasePage

class baidu(BasePage):
    kw = ['id','kw']#定位输入框
    su = ['id','su']#定位按钮

    def kw_send(self,value):
        self.send(self.kw,value)

    def su_click(self):
        self.click(self.su)