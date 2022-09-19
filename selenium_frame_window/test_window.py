from selenium import webdriver
from selenium_frame_window.base import Base
from time import sleep


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        # 代表所有窗口
        print(self.driver.window_handles)
        windos = self.driver.window_handles
        # windos 是列表，加到最后一个，从最后一个截取
        self.driver.switch_to_window(windos[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13312346782")
        sleep(5)
        self.driver.switch_to_window(windos[0])
        self.driver.find_element_by_id("TANGRAM__PSP_10__footeULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)


class TestCase():
    pass
