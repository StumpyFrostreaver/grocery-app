import time


import bs4

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.common.string_utils import StringUtils
from src.product.voila_product import VoilaProduct


class VoilaReader:
    def __init__(self):
        self.__url = None

    def with_url(self, url):
        self.__url = url
        return self

    def parse_bs(self):
        pass
    def parse(self):
        all_products = []

        if StringUtils.is_something(self.__url):
            # Set up the Selenium WebDriver in headless mode
            options = Options()
            #options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(self.__url)
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(15)

            soup = bs4.BeautifulSoup(driver.page_source, 'html')
            items = soup.find_all('div', class_='base__BoxCard-sc-1mnb0pd-5')
            print(len(items))
            return
            # time.sleep(15)
            #
            # scroll_start = 0
            # scroll_end = 1300
            # scroll_amt = scroll_end
            # total_items = 0
            # while True:
            #     # scroll the page to load more items
            #     print(f"Scroll Start: {scroll_start} Scroll End: {scroll_end}")
            #     driver.execute_script(f"window.scrollTo(0, {scroll_end});")
            #     scroll_start = scroll_end
            #     scroll_end += scroll_amt
            #     # wait for new items to load
            #     time.sleep(2)  # adjust the wait time as needed
            #
            #     # get the new number of items
            #     new_num_items = len(driver.find_elements(By.CLASS_NAME, "base__BoxCard-sc-1mnb0pd-5"))
            #     print(f"New Items: {new_num_items}")
            #
            #     # if no new items were loaded, stop scrolling
            #     if new_num_items == total_items:
            #         break
            #
            #     total_items = new_num_items

            # products = self.__parse_page(driver)
            # all_products.extend(products)
            #
            # return all_products

    def __parse_page(self, driver):
        products = []

        # Find all the product listings on the page
        results = driver.find_element(By.CLASS_NAME, "layout__Container-sc-nb1ebc-0")
        print()
        listings = results.find_elements(By.CLASS_NAME, 'base__BoxCard-sc-1mnb0pd-5')

        items_container = driver.find_element(By.XPATH, "//div[@data-synthetics='product-list']")
        items = items_container.find_elements(By.CLASS_NAME, 'base__BoxCard-sc-1mnb0pd-5')


        item_count = 1
        print(f"Found Elements: {len(items)}")
        for listing in items:
            #print(f"Processing Item: {item_count}")
            product = VoilaProduct()
            product.parse_listing(listing)
            products.append(product)
            item_count += 1

        return products
