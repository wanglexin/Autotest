"""
Created on 2020年05月07日
@author: wanglexin
"""
import time

class BaseFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, parameter):
        """
        该方法是自定义的find_element方法
        selector_by是根据什么方式来定位
        selector_value是具体的内容
        因为大部分都可以使用xpath定位所以只写了两种定位方式
        """
        element = ''
        selector_by = parameter[0]
        selector_value = parameter[1]
        if selector_by in 'x' or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 'i' or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        return element

    def find_element_bytext(self, parameter):
        """
        用来获取成功页面的信息
        主要是判断Case是否执行成功的关键
        """
        a = self.find_element(parameter).get_attribute("innerHTML")
        return a

    def click(self, parameter):
        """
        用来执行调用方法
        """
        element = self.find_element(parameter)
        element.click()

    def exe_Scrtpt(self, wxpassword):
        """
        该方法是用来调用execute_script方法，传入一个列表中嵌套着列表
        因为在调用脚本的时候无法定位到腾讯的密码输入框的定位
        所以利用坐标来进行点击操作
        因为密码长度是六位所以使用列表嵌套列表的形式，用for循环取出每个列表中的坐标
        selector_x是X坐标
        selector_y是Y坐标
        """
        for i in range(len(wxpassword)):
            selector_x = wxpassword[i][0] # 统计点击次数
            selector_y= wxpassword[i][1]
            self.driver.tap([(selector_x, selector_y)], 300)
            time.sleep(3)

    def enter_wchat(self, parameter):
        """
        进入具体链接的方法单独提取出来
        因为按摩椅启动后退款按摩椅停止时间不确定有可能因为停止时间过长而导致下一个用例执行时报错
        所以单独提取出来后每次用例执行后调用不同的椅子从而规避这个问题
        """
        self.driver.tap([(930, 2200)], 300)
        self.driver.find_element_by_xpath("//*[@text='收藏']").click()
        self.click(parameter)
        self.click(parameter)
        self.driver.implicitly_wait(5)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

