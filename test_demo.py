from seleniumbase import BaseCase
from logging import Logger
from time import sleep
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
        self.maximize_window()
        with open("thong_tin_nha_ca_nhan.txt", 'w', encoding='utf-8') as f:
            for z in range(1, 10):
                list = self.find_elements('//div[@id="product-lists-web"]/div[*]/a')
                for i in range(1, len(list)+1):
                    try:
                        self.highlight(f'//div[@id="product-lists-web"]/div[{i}]/a')
                        title = self.get_attribute(f'//div[@id="product-lists-web"]/div[{i}]/a', 'title')
                        content = self.get_text_content(f'//div[@id="product-lists-web"]/div[{i}]/a/div[2]/div[1]/div[2]', 'text')
                        self._print(f"{i} >>>>>>>>>>>> {title}")
                        self._print(f"{i} >>>>>>>>>>>> {content}")
                        f.write(f"{title}\n {content} \n\n")
                    except Exception as e:
                        e=str(e)
                        print(f'fail ==> {e}')
                        pass
                    
                self.scroll_into_view('//div[@class="re__pagination-ajax re__pagination-icon js__ajax-paging-srp-btn"]/i[@class="re__icon-chevron-right--sm"]', timeout=10)
                self.click_visible_elements('//div[@class="re__pagination-ajax re__pagination-icon js__ajax-paging-srp-btn"]/i[@class="re__icon-chevron-right--sm"]', timeout=10)
                sleep(1)

    def tearDown(self):
        return super().tearDown()