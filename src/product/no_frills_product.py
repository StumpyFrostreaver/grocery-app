import json

from selenium.webdriver.common.by import By

from src.common.selenium_utils import SeleniumUtils


class NoFrillsProduct:
    __skip_attributes = [
    ]

    def __init__(self):
        self.__name = None
        self.__brand = None

    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @property
    def as_csv(self):
        print(self.name)
        return f'{self.name}, {self.brand}'

    def parse_listing(self, listing):
        div = listing.find_element(By.TAG_NAME, 'div')
        size = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "product-name__item--package-size")
        field = div.get_attribute('data-track-products-array')
        # Parse the JSON-encoded string
        products = json.loads(field)

        for product in products:
            print(f"{product['productSKU']}, {product['productName']}, {product['productBrand']}, "
                  f"{product['productPrice']}, {product['productQuantity']}, {size}]\n")
            for field in product:
                print(f"{field} = {product[field]}")
