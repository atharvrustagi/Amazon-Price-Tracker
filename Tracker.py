import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Tracker:
    def __init__(self, headless = True) -> None:
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
    
    def search(self, search_text: str):
        self.search_text = search_text
        # wait for a while
        sleep(random.uniform(1, 2))
        # search box
        try:
            box = self.driver.find_element('id', 'twotabsearchtextbox')
            box.send_keys(search_text)
            box.send_keys(Keys.ENTER)
        except:
            print("Not loaded properly")

    def get_product_divs(self):
        divs = []
        try:
            # self.driver.find_element('css selector', f'div.s-card-container.s-overflow-hidden.aok-relative.puis-wide-grid-style.puis-wide-grid-style-t{i}.puis-include-content-margin.puis.puis-vnjufzhntlqm11zjo2xc51q7r1.s-latency-cf-section.s-card-border')
            self.driver.find_element('css selector', 'div.puis-vnjufzhntlqm11zjo2xc51q7r1')
            print('found')
            # divs = self.driver.find_elements('css selector', f'div.s-card-container.s-overflow-hidden.aok-relative.puis-wide-grid-style.puis-wide-grid-style-t{i}.puis-include-content-margin.puis.puis-vnjufzhntlqm11zjo2xc51q7r1.s-latency-cf-section.s-card-border')
            divs = self.driver.find_elements('css selector', 'div.puis-vnjufzhntlqm11zjo2xc51q7r1')
        except:
            print('not found')
            return []
        # self.driver.close()
        # filter the divs
        product_divs = []
        # words = (word.lower() for word in self.search_text.split())
        # print(list(words))
        for d in divs:
            # divtext = d.text.lower()
            # toAdd = True
            # for word in words:
            #     if word not in divtext:
            #         toAdd = False
            #         break
            # if toAdd:
            if d.text:
                product_divs.append(d)            
        return product_divs

    def close_driver(self):
        self.driver.close()


def get_products(query):
    t = Tracker(query)
    t.load_amazon()
    t.search()
    return t.get_product_divs()


if __name__ == '__main__':
    inp = input("Search query: ")
    get_products(inp)


"""

# product info cards
divs = div.s-card-container.s-overflow-hidden.aok-relative.puis-wide-grid-style.puis-wide-grid-style-t2.puis-include-content-margin.puis.puis-vnjufzhntlqm11zjo2xc51q7r1.s-latency-cf-section.s-card-border

# product name and link
product = divs[0].find_element('css selector', 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
name = product.text
link = product.get_attribute('href')

# product price (put these inside a try-catch block)
cur_price = divs[0].find_element('css selector', 'span.a-price').text
original_price = divs[0].find_element('css selector', 'span.a-price.a-text-price').text

"""
