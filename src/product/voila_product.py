from datetime import date

from selenium.webdriver.common.by import By

from src.common.string_utils import StringUtils
from src.common.selenium_utils import SeleniumUtils
from src.common.voila_utils import VoilaUtils

from src.product.base_product import BaseProduct


class VoilaProduct(BaseProduct):
    __skip_attributes = [
    ]

    def __init__(self):
        self.__date = None
        self.__name = None
        self.__size = None
        self.__price_per_unit = None
        self.__price = None
        self.__details_page = None
        self.__kosher = StringUtils.csvify_field(False)
        self.__local = StringUtils.csvify_field(False)
        self.__organic = StringUtils.csvify_field(False)
        self.__peanut_free = StringUtils.csvify_field(False)
        self.__lactose_free = StringUtils.csvify_field(False)
        self.__gluten_free = StringUtils.csvify_field(False)
        self.__vegan = StringUtils.csvify_field(False)
        self.__vegetarian = StringUtils.csvify_field(False)
        self.__sku = None

    @property
    def date(self):
        return self.__date

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
    def kosher(self):
        return self.__kosher

    @property
    def local(self):
        return self.__local

    @property
    def organic(self):
        return self.__organic

    @property
    def peanut_free(self):
        return self.__peanut_free

    @property
    def lactose_free(self):
        return self.__lactose_free

    @property
    def gluten_free(self):
        return self.__gluten_free

    @property
    def vegan(self):
        return self.__vegan

    @property
    def vegetarian(self):
        return self.__vegetarian

    @property
    def sku(self):
        return self.__sku

    @staticmethod
    def as_csv_header():
        return "date, name, size, price_per_unit, price, details_page, " \
               "kosher, local, organic, " \
               "peanut_free, lactose_free, gluten_free, vegan, vegetarian, " \
               "sku"

    @property
    def as_csv(self):
        return f"{self.date}, {self.name}, {self.size}, {self.price_per_unit}, {self.price}, {self.__details_page}, " \
               f"{self.kosher}, {self.local}, {self.organic}, " \
               f"{self.peanut_free}, {self.lactose_free}, {self.gluten_free}, {self.vegan}, {self.vegetarian}, " \
               f"{self.__sku}"

    def parse_listing(self, listing):
        self.__date = StringUtils.csvify_field(date.today().strftime("%Y-%m-%d"))

        product_attributes = SeleniumUtils.safe_find_element(listing, By.CLASS_NAME, "base__ProductAttributes-sc-1mnb0pd-25")
        if product_attributes:
            spans = product_attributes.find_elements(By.TAG_NAME, "span")
            if spans:
                for span in spans:
                    span_text = span.get_attribute("title")
                    span_text = span_text.lower()
                    if span_text == "kosher":
                        self.__kosher = StringUtils.csvify_field(True)
                    elif span_text == "local":
                        self.__local = StringUtils.csvify_field(True)
                    elif span_text == "organic":
                        self.__organic = StringUtils.csvify_field(True)
                    elif span_text == "peanut free":
                        self.__peanut_free = StringUtils.csvify_field(True)
                    elif span_text == "lactose free":
                        self.__lactose_free = StringUtils.csvify_field(True)
                    elif span_text == "gluten free":
                        self.__gluten_free = StringUtils.csvify_field(True)
                    elif span_text == "vegan":
                        self.__vegan = StringUtils.csvify_field(True)
                    elif span_text == "vegetarian":
                        self.__vegetarian = StringUtils.csvify_field(True)
                    else:
                        print(f"WARNING: Unhandled attribute '{span_text}'")

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
