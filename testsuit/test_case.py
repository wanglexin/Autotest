"""
Created on 2020年05月07日
@author: wanglexin
"""
import pytest
from appium_function.init_driver import init_driver
from pages.balance_page import BalanccePage
from pages.money_page import MoneyPage
from pages.coupons_page import CouponsPage


class TestClass(object):
    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        self.driver.quit()

    #魔豆余额支付流程
    @pytest.mark.flaky(reruns=1)
    def test_balances(self):
        balancepages = BalanccePage(self.driver)
        balancepages.enterWchat()
        balancepages.clickSpa()
        balancepages.checkMoDou()
        balancepages.checkStatr()

    #现金支付流程
    @pytest.mark.flaky(reruns=1)
    def test_Money(self):
        moneypages = MoneyPage(self.driver)
        moneypages.enterWchat()
        moneypages.clickSpa()
        moneypages.clickPay()
        moneypages.payMoney()
        moneypages.checkStatr()

    #卡券支付流程
    @pytest.mark.flaky(reruns=1)
    def test_Coupons(self):
        couponspage = CouponsPage(self.driver)
        couponspage.enterWchat()
        couponspage.clickSpa()
        couponspage.clickCoupons()
        couponspage.payCoupons()
        couponspage.checkStatr()



if __name__ == '__main__':
    pytest.main("-q test_case.py")