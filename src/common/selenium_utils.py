from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement


class SeleniumUtils:
    okay_to_not_find_elements = [
        'pricing__before-price',
        'pricing__until-date',
    ]

    @staticmethod
    def safe_button_click(button):
        try:
            button.click()
        except ElementClickInterceptedException as ex:
            print("Whoops.... error when trying to click... lets ignore...")

    @staticmethod
    def safe_find_element(element, by, name, show_warning=False) -> WebElement:
        value = None
        try:
            value = element.find_element(by, name)
        except NoSuchElementException:
            if show_warning and \
               name not in SeleniumUtils.okay_to_not_find_elements:
                print(f"\nWARN: SeleniumUtils:safe_find_element: Could not find element \'{name}\' in HTML:\n"
                      f"{element.get_attribute('outerHTML')}\n")
        return value

    # @staticmethod
    # def safe_find_elements(element, by, name, show_warning=False):
    #     values = None
    #     try:
    #         values = element.find_elements(by, name)
    #     except NoSuchElementException:
    #         if show_warning and \
    #                 name not in SeleniumUtils.okay_to_not_find_elements:
    #             print(f"\nWARN: SeleniumUtils:safe_find_element: Could not find element \'{name}\' in HTML:\n"
    #                   f"{element.get_attribute('outerHTML')}\n")
    #     return values

    @staticmethod
    def safe_find_element_text(element, by, name, show_warning=False) -> str:
        value = SeleniumUtils.safe_find_element(element, by, name, show_warning)
        if value is None:
            return ""
        return value.text
