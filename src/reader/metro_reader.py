import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.product.product import MetroProduct


class MetroReader:
    def __init__(self):
        self.__url = None

    def with_url(self, url):
        self.__url = url
        return self

    def parse(self):
        all_products = []

        # Set up the Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(self.__url)
        time.sleep(3)
        click_me = driver.find_element(By.CLASS_NAME, 'cookie-consent--container')
        button = click_me.find_element(By.TAG_NAME, 'button')
        button.click()

        more_to_read = True

        while more_to_read:
            products = self.__parse_page(driver)
            all_products.extend(products)

            cp_labels = driver.find_elements(By.CLASS_NAME, 'cta-primary')
            for cp_label in cp_labels:
                more_to_read = False
                if cp_label.text == "Next":
                    more_to_read = True
                    try:
                        if 'disabled' in cp_label.get_attribute('outerHTML'):
                            more_to_read = False
                        else:
                            cp_label.click()
                    except:
                        more_to_read = False
                    break

        return all_products

    def __parse_page(self, driver):
        products = []

        # Find all the product listings on the page
        results = driver.find_element(By.CLASS_NAME, "products-search--grid")
        listings = results.find_elements(By.CLASS_NAME, 'tile-product')

        for listing in listings:
            product = MetroProduct()
            product.parse_listing(listing)
            products.append(product)

        return products