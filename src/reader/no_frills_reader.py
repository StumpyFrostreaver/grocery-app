import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.common.string_utils import StringUtils
from src.product.no_frills_product import NoFrillsProduct


class NoFrillsReader:
    def __init__(self):
        self.__url = None

    def with_url(self, url):
        self.__url = url
        return self

    def parse(self):
        all_products = []

        if StringUtils.is_something(self.__url):
            # Set up the Selenium WebDriver in headless mode
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(self.__url)

            # Wait for the page to load
            listings = None
            page = 0

            more_to_read = True
            while more_to_read:
                while listings is None:
                    time.sleep(5)
                    # try:
                    # Find all the product listings on the page
                    listings = driver.find_element(By.CLASS_NAME, 'product-grid__results__products')
                    self.__parse_page(listings)
                    print("page loaded")
                    # except NoSuchElementException:
                    #     print("no listings yet")
                lis = listings.find_elements(By.CLASS_NAME, 'product-tile-group__list__item')
                print(f"there are {len(lis)} items")
                page += 1
                if page == 1:
                    button = driver.find_element(By.CLASS_NAME, "modal-dialog__content__close")
                    button.click()
                    button = driver.find_element(By.CLASS_NAME, "lds__privacy-policy__btnClose")
                    button.click()

                self.__parse_page(listings)
            return all_products

    def __parse_page(self, driver):
        products = []

        # Find all the product listings on the page
        # TODO: Change to use SAFE FIND BY ELEMENT
        results = driver.find_element(By.CLASS_NAME, "products-search--grid")
        listings = results.find_elements(By.CLASS_NAME, 'tile-product')

        for listing in listings:
            product = NoFrillsProduct()
            product.parse_listing(listing)
            products.append(product)

        return products


