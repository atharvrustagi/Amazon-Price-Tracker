import pandas as pd
from Tracker import Tracker

t = Tracker(headless=False)
t.load_amazon()

inp = input("Search for: ")
t.search(inp)

divs = t.get_product_divs()

data = {
    'Name': [],
    'Current Price': [],
    'Original Price': [],
    'Link': []
}

# make a csv file
for div in divs:
    product = div.find_element('css selector', 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
    name = product.text
    link = product.get_attribute('href')

    cur_price, original_price = '', ''
    try:
        cur_price = div.find_element('css selector', 'span.a-price').text
    except:
        cur_price = '-'
    try:
        original_price = div.find_element('css selector', 'span.a-price.a-text-price').text
    except:
        original_price = cur_price
    
    data['Name'].append(name)
    data['Current Price'].append(cur_price)
    data['Original Price'].append(original_price)
    data['Link'].append(link)

t.close_driver()

df = pd.DataFrame(data)
print(df)
df.to_csv(f'{inp.replace(" ", "_")}.csv')
