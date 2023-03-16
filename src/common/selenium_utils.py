from selenium.common.exceptions import NoSuchElementException


class SeleniumUtils:
    okay_to_not_find_elements = [
        'pricing__before-price',
        'pricing__until-date',
    ]
    @staticmethod
    def safe_find_element(element, by, name):
        value = None
        try:
            value = element.find_element(by, name)
        except NoSuchElementException:
            if name not in SeleniumUtils.okay_to_not_find_elements:
                print(f"WARN: SeleniumUtils:safe_find_element: Could not find element \'{name}\' in HTML:\n\n"
                      f"{element.get_attribute('outerHTML')}")
        return value

    @staticmethod
    def safe_find_element_text(element, by, name):
        value = SeleniumUtils.safe_find_element(element, by, name)
        if value is None:
            return ""
        return value.text
