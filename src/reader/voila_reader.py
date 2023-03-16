import time

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
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(self.__url)
            # site_content = driver.find_element(By.CLASS_NAME, 'site--content')
            # print(site_content.get_attribute('outerHTML'))

            current_scroll = 1600
            scroll_to = 0
            scroll_amount = 1200
            page = 1

            while True:
                print(f'\n\nPage {page}:\n\n\n')
                products = self.__parse_page(driver)
                scroll_to = current_scroll + scroll_amount
                driver.execute_script(f"window.scrollTo(0, {scroll_to});")
                time.sleep(1)
                current_scroll = scroll_to
                if len(all_products) > 0 and len(products) > 0:
                    if all_products[len(all_products)-1].as_csv == products[len(products)-1].as_csv:
                        break
                else:
                    print(f"** WARNING ** -- A Collection Is Empty: all_products count: {len(all_products)}  "
                          f"products count: {len(products)}")

                all_products.extend(products)
                print(f"Currently at {len(all_products)} total items.")
                page += 1

        return all_products

    def __parse_page(self, driver):
        products = []

        # # Find all the product listings on the page
        # results = driver.find_element(By.CLASS_NAME, "layout__Container-sc-nb1ebc-0")
        # print()
        # listings = results.find_elements(By.CLASS_NAME, 'base__BoxCard-sc-1mnb0pd-5')
        #
        # items_container = driver.find_element(By.XPATH, "//div[@data-synthetics='product-list']")
        items = driver.find_elements(By.CLASS_NAME, 'base__BoxCard-sc-1mnb0pd-5')

        item_count = 1
        print(f"Found Elements: {len(items)}")
        for listing in items:
            print(f"Processing Item: {item_count}")
            product = VoilaProduct()
            product.parse_listing(listing)
            products.append(product)
            item_count += 1

        return products
