"""
Created on 2020年05月07日
@author: wanglexin
"""
import time
from appium_function.base_function import BaseFunction


class BalanccePage(BaseFunction):
    spa = ['xpath', "//span[text()=\"唤醒身体\"]"]
    check = ['xpath', "//*[@id='checked']"]
    statr = ["id", "successOrderMsg"]
    pay = ['xpath', "//div[text()=\"立即启动\"]"]
    connect = ['xpath', "//*[contains(@text,'89861118272032557798')]"]

    def enterWchat(self):
        self.enter_wchat(self.connect)

    def clickSpa(self): # 点击套餐的操作
        self.click(self.spa)

    def checkMoDou(self): # 检查魔豆开关是否打开
        time.sleep(5)
        TorF = self.find_element(self.check).get_attribute("checked")
        if TorF == "true":
            self.click(self.pay)
        else:
            self.find_element(self.check).click()
            self.click(self.pay)

    def checkStatr(self):
        """
        该方法用于检查是否启动成功
        后期加入logger日志，现将日志输出到控制台
        """
        time.sleep(15)
        statrsuccess = self.find_element_bytext(self.statr)
        assert "元" in statrsuccess
