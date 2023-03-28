import json
from datetime import date

from selenium.webdriver.common.by import By

from src.common.string_utils import StringUtils
from src.common.selenium_utils import SeleniumUtils

from src.product.base_product import BaseProduct


class NoFrillsProduct(BaseProduct):
    __skip_attributes = [
        "productPosition",
    ]

    def __init__(self):
        super().__init__()
        self.__date = None
        self.__article_no = None
        self.__product_id = None
        self.__list_price = None
        self.__list_price_unit = None
        self.__comparison_price = None
        self.__comparison_price_unit = None
        self.__sku = None
        self.__name = None
        self.__brand = None
        self.__catalog = None
        self.__vendor = None
        self.__price = None
        self.__quantity = None
        self.__deal_badge = None
        self.__loyalty_badge = None
        self.__text_badge = None
        self.__order_id = None
        self.__variant = None
        self.__sub_product = None
        self.__rating = None
        self.__size = None
        self.__out_of_stock = StringUtils.csvify_field(True)

    @property
    def date(self):
        return self.__date

    @property
    def article_no(self):
        return self.__article_no

    @property
    def product_id(self):
        return self.__product_id

    @property
    def list_price(self):
        return self.__list_price

    @property
    def list_price_unit(self):
        return self.__list_price_unit

    @property
    def comparison_price(self):
        return self.__comparison_price

    @property
    def comparison_price_unit(self):
        return self.__comparison_price_unit
    @property
    def sku(self):
        return self.__sku

    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @property
    def catalog(self):
        return self.__catalog

    @property
    def vendor(self):
        return self.__vendor

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def deal_bade(self):
        return self.__deal_badge

    @property
    def loyalty_badge(self):
        return self.__loyalty_badge

    @property
    def text_badge(self):
        return self.__text_badge

    @property
    def order_id(self):
        return self.__order_id

    @property
    def variant(self):
        return self.__variant

    @property
    def sub_product(self):
        return self.__sub_product

    @property
    def rating(self):
        return self.__rating

    @property
    def size(self):
        return self.__size

    @property
    def out_of_stock(self):
        return self.__out_of_stock

    @staticmethod
    def as_csv_header():
        return "date, article_no, product_id, " \
               "list_price, list_price_unit, comparison_price, comparison_price_unit, " \
               "sku, name, brand, catalog, vendor, price, " \
               "quantity, deal_badge, loyalty_badge, text_badge, order_id, " \
               "variant, sub_product, rating, size, out_of_stock"

    @property
    def as_csv(self):
        return f"{self.date}, {self.article_no}, {self.product_id}, " \
               f"{self.list_price}, {self.list_price_unit}, {self.comparison_price}, {self.comparison_price_unit}, " \
               f"{self.sku}, {self.name}, {self.brand}, {self.catalog}, {self.vendor}, {self.price}, " \
               f"{self.quantity}, {self.deal_bade}, {self.loyalty_badge}, {self.text_badge}, {self.order_id}, " \
               f"{self.variant}, {self.sub_product}, {self.rating}, {self.size}, {self.out_of_stock}"

    def parse_listing(self, listing):
        self.__date = StringUtils.csvify_field(date.today().strftime("%Y-%m-%d"))
        size = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "product-name__item--package-size")
        self.__size = StringUtils.csvify_field(size)

        div = listing.find_element(By.TAG_NAME, "div")
        self.__article_no = StringUtils.csvify_field(div.get_attribute("data-track-article-number"))
        self.__product_id = StringUtils.csvify_field(div.get_attribute("data-track-product-id"))

        self.__list_price = StringUtils.csvify_field(SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "selling-price-list__item__price--now-price__value"))
        self.__list_price_unit = StringUtils.csvify_field(SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "selling-price-list__item__price--now-price__unit"))
        self.__comparison_price = StringUtils.csvify_field(SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "comparison-price-list__item__price__value"))
        self.__comparison_price_unit = StringUtils.csvify_field(SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "comparison-price-list__item__price__unit"))

        product_button_group = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "product-button-group")

        # The ADD button has all the details (including quantity), so it's the best place to get the information
        # from...
        dtpa_element = SeleniumUtils.safe_find_element(product_button_group, By.CLASS_NAME, "common-button")

        # ...if the item is out of stock, the ADD button is not accessible, so lets get the info from the
        # 'product-tracking' spot...
        if dtpa_element is None:
            dtpa_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "product-tracking")
            self.__out_of_stock = StringUtils.csvify_field(True)

        dtpa = dtpa_element.get_attribute("data-track-products-array")
        # Parse the JSON-encoded string
        if dtpa:
            products_json = json.loads(dtpa)

            if len(products_json) > 0:
                product_json = products_json[0]
                if len(products_json) > 1:
                    print("WARNING: Found more then 1 item when expecting only 1. Only handling the first item:\n"
                          f"{products_json}")
                for key in product_json:
                    value = StringUtils.csvify_field(product_json[f"{key}"])

                    if key == "productSKU":
                        self.__sku = value
                    elif key == "productName":
                        self.__name = value
                    elif key == "productBrand":
                        self.__brand = value
                    elif key == "productCatalog":
                        self.__catalog = value
                    elif key == "productVendor":
                        self.__vendor = value
                    elif key == "productPrice":
                        self.__price = value
                    elif key == "productQuantity":
                        self.__quantity = value
                    elif key == "dealBadge":
                        self.__deal_badge = value
                    elif key == "loyaltyBadge":
                        self.__loyalty_badge = value
                    elif key == "textBadge":
                        self.__text_badge = value
                    elif key == "productOrderId":
                        self.__order_id = value
                    elif key == "productVariant":
                        self.__variant = value
                    elif key == "subProduct":
                        self.__sub_product = value
                    elif key == "productRating":
                        self.__rating = value
                    elif key == "productBrand":
                        self.__brand = value
                    elif key in self.__skip_attributes:
                        pass
                        # print(f"Skipping attribute: '{key}' with value: '{value}'")
                    else:
                        print(f"Unknown attribute: '{key}' with value: '{value}'")
            else:
                print("ERROR: Expected 1 json element, found 0.")
        else:
            raise Exception(f"ERROR: Could not find 'data-track-products-array' in HTML:\n"
                            f"{listing.get_attribute('outerHTML')}")
