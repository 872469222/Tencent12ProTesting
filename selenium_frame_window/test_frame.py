from selenium_frame_window.base import Base

from time import sleep

from selenium_frame_window.base import Base


class TestJs(Base):
    def test_frmae(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("droppable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)






