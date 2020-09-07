"""
Created on 2020年05月07日
@author: wanglexin
"""
from appium import webdriver
import time


def init_driver():
    """
    最基本的封装了安卓手机的一些内容
    包括通过微信进入H5页面的一些流程
    这里的代码直接可以进入到页面中且已经切换到WEBVIEW了
    """
    desired_caps={}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '9a1fb88b'
    desired_caps['noReset'] = 'True'
    desired_caps['appPackage'] = 'com.tencent.mm'  # 获取被测APP的包名
    desired_caps['appActivity'] = '.ui.LauncherUI'
    desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)

    return driver
if __name__ == '__main__':
    a = init_driver()
    a.main()