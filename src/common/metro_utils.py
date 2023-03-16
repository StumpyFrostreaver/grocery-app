import re

class MetroUtils:
    @staticmethod
    def get_price_from_price_string(price_string):
        price = ''
        search_results = re.search('\$([0-9.]+)', price_string)
        if search_results:
            price = search_results.group(1)
        return price

    @staticmethod
    def get_date_from_date_string(price_string):
        price = ''
        search_results = re.search('\$([0-9.]+)', price_string)
        if search_results:
            price = search_results.group(1)
        return price
