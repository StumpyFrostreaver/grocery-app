from selenium.webdriver.common.by import By

from src.common.metro_utils import MetroUtils
from src.common.selenium_utils import SeleniumUtils
from src.common.string_utils import StringUtils


class MetroProduct:
    __skip_attributes = [
        "class",
        "data-unit-increment",
        "data-min-qty",
        "data-max-qty",
        "data-product-deletable",
        "data-is",
        "data-substitution-permission",
        "data-criteo-on-load-beacon",
        "data-criteo-on-click-beacon",
        "data-criteo-on-view-beacon",
        "data-criteo-on-basket-change-beacon",
        "data-criteo-on-wish-list-beacon",
        "data-criteo-format-level-on-load-beacon",
        "data-criteo-format-level-on-view-beacon",
    ]

    def __init__(self):
        self.__code = None
        self.__inactive = None
        self.__name = None
        self.__category = None
        self.__category_id = None
        self.__category_url = None
        self.__brand = None
        self.__age_restriction = None
        self.__alcohol = None
        self.__price = None
        self.__price_per_unit = None
        self.__price_before_sale = None
        self.__on_sale_until = None

    @property
    def code(self):
        return self.__code

    @property
    def inactive (self):
        return self.__inactive

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def category_id(self):
        return self.__category_id

    @property
    def category_url(self):
        return self.__category_url

    @property
    def brand(self):
        return self.__brand

    @property
    def age_restriction(self):
        return self.__age_restriction

    @property
    def alcohol(self):
        return self.__alcohol

    @property
    def price(self):
        return self.__price

    @property
    def price_per_unit(self):
        return self.__price_per_unit

    @property
    def price_before_sale(self):
        return self.__price_before_sale

    @property
    def on_sale_until(self):
        return self.__on_sale_until

    @staticmethod
    def as_csv_header():
        return "code, inactive, name, category, category_id, category_url, " \
               "brand, age_restriction, alcohol, price, price_per_unit, " \
               "price_before_sale, on_sale_until"

    @property
    def as_csv(self):
        return f"{self.code}, {self.inactive}, {self.name}, {self.category}, {self.category_id}, {self.category_url}, " \
               f"{self.brand}, {self.age_restriction}, {self.alcohol}, {self.price}, {self.price_per_unit}, " \
               f"{self.price_before_sale}, {self.on_sale_until}"

    def parse_listing(self, listing):
        attributes = listing.get_property("attributes")

        # Loop through the list and print the name and value of each attribute
        for attribute in attributes:
            key = attribute["name"]
            value = StringUtils.csvify_field(attribute["value"])

            if key == "data-product-code":
                self.__code = value
            elif key == "data-is-inactive":
                self.__inactive = value
            elif key == "data-product-name":
                self.__name = value
            elif key == "data-product-category":
                self.__category = value
            elif key == "data-product-category-id":
                self.__category_id = value
            elif key == "data-category-url":
                self.__category_url = value
            elif key == "data-product-brand":
                self.__brand = value
            elif key == "data-age-restriction":
                self.__age_restriction = value
            elif key == "data-product-alcohol":
                self.__alcohol = value
            elif key in self.__skip_attributes:
                pass
                # print(f"Skipping attribute: '{key}' with value: '{value}'")
            else:
                print(f"Unknown attribute: '{key}' with value: '{value}'")

        # We can consolidate this, but for now, its nice to debug...
        price = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "price-update")
        ppu = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "pricing__secondary-price")
        price_before_sale = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "pricing__before-price")
        on_sale_until = SeleniumUtils.safe_find_element_text(listing, By.CLASS_NAME, "pricing__until-date")

        self.__price = StringUtils.csvify_field(price)
        self.__price_per_unit = StringUtils.csvify_field(ppu)
        self.__price_before_sale = StringUtils.csvify_field(MetroUtils.get_price_from_price_string(price_before_sale))
        self.__on_sale_until = StringUtils.csvify_field(on_sale_until)

        return self
