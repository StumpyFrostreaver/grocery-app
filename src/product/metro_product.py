from selenium.webdriver.common.by import By


class MetroProduct:
    __skip_attributes = [
        'class',
        'data-min-qty',
        'data-max-qty',
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
        # Get a list of all attribute names of the div element
        divs = listing.find_elements(By.TAG_NAME, 'div')
        attributes = listing.get_property("attributes")

        # Loop through the list and print the name and value of each attribute
        print ("\n\n\n\n=-----------> ATTRIBUTES\n")
        for attribute in attributes:
            key = attribute['name']
            value = attribute['value']
            if key == 'data-product-name':
                self.__name = value
            elif key == 'data-product-brand':
                self.__brand = value
            elif key in self.__skip_attributes:
                print (f'Skipping attribute: \'{key}\'')
            else:
                print (f'Unknown attribute: \'{key}\'')
        return self
