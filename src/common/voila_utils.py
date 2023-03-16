import re


class VoilaUtils:
    @staticmethod
    def get_sku_from_href(href):
        search_results = re.search(r'/products/([a-zA-Z0-9]+)\b', href)
        return search_results.group(1)
