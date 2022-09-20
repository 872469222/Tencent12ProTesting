from selenium import webdriver
import os


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser =="firefox":
            self.driver=webdriver.remote()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
