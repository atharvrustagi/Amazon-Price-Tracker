import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Tracker:
    def __init__(self, search_text: str, headless = True) -> None:
        self.search_text = search_text
        op = webdriver.ChromeOptions()
        if headless:
            op.add_argument('headless')
        self.driver = webdriver.Chrome(op)
    
    def load_amazon(self):
        # wait for a while
        sleep(random.uniform(1, 2))
        # load
        self.driver.get('https://www.amazon.in')
        self.driver.maximize_window()
    
    def search(self):
        # wait for a while
        sleep(random.uniform(1, 2))
        # search box
        try:
            box = self.driver.find_element('id', 'twotabsearchtextbox')
            box.send_keys(self.search_text)
            box.send_keys(Keys.ENTER)
        except:
            print("Not loaded properly")

    def get_product_divs(self):
        product_divs = []
        try:
            # self.driver.find_element('css selector', f'div.s-card-container.s-overflow-hidden.aok-relative.puis-wide-grid-style.puis-wide-grid-style-t{i}.puis-include-content-margin.puis.puis-vnjufzhntlqm11zjo2xc51q7r1.s-latency-cf-section.s-card-border')
            self.driver.find_element('css selector', 'div.puis-vnjufzhntlqm11zjo2xc51q7r1')
            print('found')
            # product_divs = self.driver.find_elements('css selector', f'div.s-card-container.s-overflow-hidden.aok-relative.puis-wide-grid-style.puis-wide-grid-style-t{i}.puis-include-content-margin.puis.puis-vnjufzhntlqm11zjo2xc51q7r1.s-latency-cf-section.s-card-border')
            product_divs = self.driver.find_elements('css selector', 'div.puis-vnjufzhntlqm11zjo2xc51q7r1')
        except:
            print('not found')
        # self.driver.close()
        return product_divs


def get_products(query):
    t = Tracker(query)
    t.load_amazon()
    t.search()
    return t.get_product_divs()


if __name__ == '__main__':
    inp = input("Search query: ")
    get_products(inp)
