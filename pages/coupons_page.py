"""
Created on 2020年05月07日
@author: wanglexin
"""
import time
from appium_function.base_function import BaseFunction


class CouponsPage(BaseFunction):
    spa = ['xpath', "//span[text()=\"通行气血\"]"]
    selectcoupons = ['xpath', "//span[text()=\"未使用\"]"]
    coupons = ['xpath', "//div[text()=\"可用时间：全天可用\"]"]
    pay = ['xpath', "//div[text()=\"立即启动\"]"]
    statr = ["id", "successOrderMsg"]
    connect = ['xpath', "//*[contains(@text,'898607B2091780918471')]"]

    def enterWchat(self):
        self.enter_wchat(self.connect)

    def clickSpa(self):#点击套餐
        self.click(self.spa)

    def clickCoupons(self):#先进入优惠券选择页面，选择一张优惠券
        time.sleep(3)
        self.click(self.selectcoupons)
        time.sleep(3)
        selectcoupons = self.find_element_bytext(self.coupons)
        if "可用时间" in selectcoupons:
            self.click(self.coupons)
        else:
            raise RuntimeError("优惠券不存在！")

    def payCoupons(self):#调用支付
        time.sleep(3)
        self.click(self.pay)

    def checkStatr(self):#检查是否启动成功
        time.sleep(15)
        statrsuccess = self.find_element_bytext(self.statr)
        assert "元" in statrsuccess
