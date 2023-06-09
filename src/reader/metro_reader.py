import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.common.selenium_utils import SeleniumUtils
from src.common.string_utils import StringUtils

from src.reader.base_reader import BaseReader
from src.product.metro_product import MetroProduct


class MetroReader(BaseReader):
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

            # may not be needed (this time.sleep(3))
            time.sleep(3)

            click_me = SeleniumUtils.safe_find_element(driver, By.CLASS_NAME, "cookie-consent--container")
            if click_me:
                button = click_me.find_element(By.TAG_NAME, "button")
                button.click()

            more_to_read = True

            page = 0
            while more_to_read:
                page += 1
                products = self.__parse_page(driver)
                all_products.extend(products)

                cp_labels = driver.find_elements(By.CLASS_NAME, "cta-primary")
                for cp_label in cp_labels:
                    more_to_read = False
                    if cp_label.text == "Next":
                        more_to_read = True
                        try:
                            if "disabled" in cp_label.get_attribute("outerHTML"):
                                more_to_read = False
                            else:
                                cp_label.click()
                        except:
                            more_to_read = False
                        break

                print(f"Finished Page {page}. {len(all_products)} so far...")
            return all_products

    def __parse_page(self, driver):
        products = []

        # Find all the product listings on the page
        results = driver.find_element(By.CLASS_NAME, "products-search--grid")
        listings = results.find_elements(By.CLASS_NAME, "tile-product")

        for listing in listings:
            product = MetroProduct()
            product.parse_listing(listing)
            products.append(product)

        return products
