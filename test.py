from selenium import webdriver
from time import sleep
from threading import Thread


def get_price(link, prices, idx):
	op = webdriver.ChromeOptions()
	op.add_argument('headless')
	driver = webdriver.Chrome(op)
	# any amazon product link
	sleep(2)

	driver.get(link)
	driver.find_elements('tag', 'div')
	
	price_info = driver.find_element('id', 'corePriceDisplay_desktop_feature_div').text
	prices[idx] = price_info


links = [
	'https://www.amazon.in/GeForce-Graphics-IceStorm-Advanced-ZT-A30610H-10MLHR/dp/B097YW4FW9/',
	# 'https://www.amazon.in/Zotac-Gaming-GeForce-4060-Spider-Man/dp/B0C86FF325/'
]

prices = [None] * len(links)
thrs = []
for i, link in enumerate(links):
	thr = Thread(target=get_price, args=(link, prices, i))
	thr.start()
	thrs.append(thr)

for thr in thrs:
	thr.join()

print('\n\n\n', prices)

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