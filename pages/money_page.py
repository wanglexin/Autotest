"""
Created on 2020年05月07日
@author: wanglexin
"""
import time
from appium_function.base_function import BaseFunction


class MoneyPage(BaseFunction):
    spa = ['xpath', "//span[text()=\"唤醒身体\"]"]
    check = ['xpath', "//*[@id='checked']"]
    wxpassword = [ # 后期考虑用其他方式来管理密码，但目前为了快速完成代码用这种方式，等待后期优化,前六位是支付密码，后一位是点击
        ["*", "*"],
        ["*", "*"],
        ["*", "*"],
        ["*", "*"],
        ["*", "*"],
        ["*", "*"],
        ["*", "*"]
    ]
    pay = ['xpath', "//div[text()=\"立即启动\"]"]
    statr = ["id", "successOrderMsg"]
    connect = ['xpath', "//*[contains(@text,'89860407091871837730')]"]

    def enterWchat(self):#进入微信
        self.enter_wchat(self.connect)

    def clickSpa(self):#点击套餐
        self.click(self.spa)

    def clickPay(self):
        """
        点击支付按钮
        这步要注意业务逻辑
        因为现在默认是每次进入时会打开使用魔豆的开关，如果有魔豆金额大于套餐的情况下就不会进入现金支付流程
        所以需要先关闭按钮才会确保进入现金支付流程
        """
        time.sleep(5)
        TorF = self.find_element(self.check).get_attribute("checked")
        if TorF == "true":
            self.find_element(self.check).click()
            self.click(self.pay)
        else:
            self.click(self.pay)

    def payMoney(self):#调用支付
        time.sleep(5)
        self.exe_Scrtpt(self.wxpassword)

    def checkStatr(self):#检查是否启动成功
        time.sleep(15)
        statrsuccess = self.find_element_bytext(self.statr)
        assert "元" in statrsuccess
