import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.common.string_utils import StringUtils

from src.reader.base_reader import BaseReader
from src.product.voila_product import VoilaProduct


class VoilaReader(BaseReader):
    def __init__(self, job):
        super().__init__(job)

    def parse(self):
        all_products = []

        if StringUtils.is_something(self.url):
            # Set up the Selenium WebDriver in headless mode
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)

            current_scroll = 1600
            scroll_to = 0
            scroll_amount = 1200
            page = 1

            while True:
                products = self.__parse_page(driver)
                scroll_to = current_scroll + scroll_amount
                driver.execute_script(f"window.scrollTo(0, {scroll_to});")
                time.sleep(1)
                current_scroll = scroll_to
                if len(all_products) > 0 and len(products) > 0:
                    if all_products[len(all_products)-1].as_csv == products[len(products)-1].as_csv:
                        break
                    else:
                        pass
                else:
                    print(f"** WARNING ** -- A Collection Is Empty: all_products count: {len(all_products)}  "
                          f"products count: {len(products)}")

                all_products.extend(products)
                print(f"Page {page}: Currently at {len(all_products)} total items.")
                page += 1

        seen_skus = []
        filtered_products = []
        for product in all_products:
            if product.sku not in seen_skus:
                filtered_products.append(product)
                seen_skus.append(product.sku)
        print(f"Read {len(all_products)} items but filtered list to {len(filtered_products)} unique items.")
        return filtered_products

    def __parse_page(self, driver):
        products = []
        items = driver.find_elements(By.CLASS_NAME, "base__BoxCard-sc-1mnb0pd-5")

        item_count = 1
        for listing in items:
            product = VoilaProduct()
            product.parse_listing(listing)
            products.append(product)
            item_count += 1

        return products
