from selenium.webdriver.common.by import By

from src.common.selenium_utils import SeleniumUtils
from src.common.string_utils import StringUtils
from src.common.voila_utils import VoilaUtils


class VoilaProduct:
    __skip_attributes = [
    ]

    def __init__(self):
        self.__name = None
        self.__size = None
        self.__price_per_unit = None
        self.__price = None
        self.__details_page = None
        self.__sku = None

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def price_per_unit(self):
        return self.__price_per_unit

    @property
    def price(self):
        return self.__price

    @property
    def details_page(self):
        return self.__details_page

    @property
    def sku(self):
        return self.__sku

    @staticmethod
    def as_csv_header():
        return "name, size, price_per_unit, price, details_page, sku"

    @property
    def as_csv(self):
        return f"{self.name}, {self.size}, {self.price_per_unit}, {self.price}, {self.__details_page}, {self.__sku}"

    def parse_listing(self, listing):
        name_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "text__Text-sc-6l1yjp-0")
        self.__name = StringUtils.csvify_field(name_element.text)

        size_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "fop__SizeText-sc-1e1rsqo-2")
        self.__size = StringUtils.csvify_field(size_element.text)

        price_per_unit_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "fop__PricePerText-sc-1e1rsqo-3")
        self.__price_per_unit = StringUtils.csvify_field(price_per_unit_element.text)

        price_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "base__Price-sc-1mnb0pd-29")
        self.__price = StringUtils.csvify_field(price_element.text)

        sku_element = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "link__Link-sc-14ymsi2-0")
        sku_href = sku_element.get_attribute("href")
        self.__details_page = StringUtils.csvify_field(sku_href)
        self.__sku = StringUtils.csvify_field(VoilaUtils.get_sku_from_href(sku_href))

        return self
