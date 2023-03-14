from selenium.common.exceptions import NoSuchElementException

class SeleniumUtils:
    @staticmethod
    def safe_find_element(element, by, name):
        value = None
        try:
            value = element.find_element(by, name)
        except NoSuchElementException:
            print(f"SeleniumUtils:safe_find_element: {name}")
        return value

    @staticmethod
    def safe_find_element_text(element, by, name):
        value = SeleniumUtils.safe_find_element(element, by, name)
        if value is None:
            return ""
        return value.text
