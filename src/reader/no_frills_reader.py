import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.common.selenium_utils import SeleniumUtils
from src.common.string_utils import StringUtils

from src.reader.base_reader import BaseReader
from src.product.no_frills_product import NoFrillsProduct


class NoFrillsReader(BaseReader):
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

            # Wait for the page to load
            listings = None
            page = 0

            more_to_read = True
            while more_to_read:
                while listings is None:
                    try:
                        # Find all the product listings on the page
                        time.sleep(2)
                        listings = driver.find_element(By.CLASS_NAME, "product-grid__results__products")
                    except NoSuchElementException:
                        print("No listings found yet on this page...")
                lis = listings.find_elements(By.CLASS_NAME, "product-tile-group__list__item")
                print(f"Page Loaded... There are {len(lis)} items on this page.")
                listings = None
                page += 1
                if page == 1:
                    time.sleep(5)
                    button = driver.find_element(By.CLASS_NAME, "modal-dialog__content__close")
                    button.click()
                    button = driver.find_element(By.CLASS_NAME, "lds__privacy-policy__btnClose")
                    button.click()

                load_more_button = SeleniumUtils.safe_find_element(driver, By.CLASS_NAME, "load-more-button")
                if load_more_button:
                    button = SeleniumUtils.safe_find_element(load_more_button, By.CLASS_NAME, "primary-button")
                    if button:
                        button.click()
                    else:
                        print("ERROR: Could not find a button on the 'load-more-button' element.")
                        more_to_read = False
                else:
                    print("No more 'load-more-button' elements.")
                    more_to_read = False

            all_products = self.__parse_page(driver)
            return all_products

    def __parse_page(self, driver):
        products = []
        error_count = 0
        error_listings = ''
        all_listings = ''

        # Find all the product listings on the page
        # TODO: Change to use SAFE FIND BY ELEMENT
        results = SeleniumUtils.safe_find_element(driver, By.CLASS_NAME, "product-grid__results__products")
        listings = results.find_elements(By.CLASS_NAME, "product-tile-group__list__item")

        listing_count = 0
        for listing in listings:
            listing_count += 1
            product = NoFrillsProduct()
            try:
                product.parse_listing(listing)
                products.append(product)
                all_listings += f"Listing: {listing_count} -- {listing.get_attribute('outerHTML')}\n"
            except Exception as ex:
                error_count += 1
                error_listings += f"{listing_count} "
                all_listings += f"ERR - Listing: {listing_count} -- {listing.get_attribute('outerHTML')}\n"
                print(f"Listing: {listing_count} {ex}")

        print(f"Processed {listing_count} records with {error_count} errors.\nErrors on Listings: {error_listings}")
        with open('../csv_files/mark/nofrills_all_listings.csv', 'w', newline='') as file:
            file.write(all_listings)
        return products


