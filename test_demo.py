from seleniumbase import BaseCase
from logging import Logger
BaseCase.main(__name__, __file__)

class TestSimpleLogin(BaseCase):
    def test_simple_login(self):
        self.open("https://seleniumbase.io/simple/login")
        self.type("#username", "demo_user")
        self.type("#password", "secret_pass")
        self.click('a:contains("Sign in")')
        self.assert_exact_text("Welcome!", "h1")
        self.assert_element("img#image1")
        self.highlight("#image1")
        self.click_link("Sign out")
        self.assert_text("signed out", "#top_message")

class CrawlDataFile(BaseCase):
    def test1(self):
        self.open("https://batdongsan.com.vn/ban-nha-rieng")
        list = self.find_elements('//div[@id="product-lists-web"]/div[*]/a')
        for i in list:
            try:
                self.highlight(i)
                title = self.get_attribute(i, 'title')
                print(title)
                # self.get_attribute(selector=i, attribute='title')
            except:
                print('fail')
                pass