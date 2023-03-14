# from base_reader import BaseReader
#
#
# class NoFrillsReader(BaseReader):
#     def parse(self):
#         # Set up the Selenium WebDriver
#         driver = webdriver.Chrome()
#         driver.get(url)
#
#         # Wait for the page to load
#         time.sleep(5)
#
#         # Find all the product listings on the page
#         listings = driver.find_element(By.CLASS_NAME, 'site-content')
#         divs = listings.find_elements(By.TAG_NAME, 'div')
#         field = divs[0].get_attribute('data-track-products-array')
#
#         # Parse the JSON-encoded string
#         products = json.loads(field)
#
#

#######################################################################################################
##
## FROM MAIN
##
## ------------------------

# import json
# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.actions import
# from selenium.webdriver.support import expected_conditions as EC
#
# from src.selenium_utils import SeleniumUtils
#
# # URL to be scraped
# url = "https://www.nofrills.ca/search?search-bar=coffee"
#
# count = 0
# page = 0
#
# # Set up the Selenium WebDriver in headless mode
# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver.get(url)
#
# # Wait for the page to load
# listings = None
#
# more_to_read = True
# while more_to_read:
#
#     while listings is None:
#         time.sleep(5)
#         try:
#             # Find all the product listings on the page
#             listings = driver.find_element(By.CLASS_NAME, 'product-grid__results__products')
#             print("page loaded")
#         except:
#             print("no listings yet")
#     lis = listings.find_elements(By.CLASS_NAME, 'product-tile-group__list__item')
#     print(f"there are {len(lis)} items")
#
#     page += 1
#
#     # Wait for the window to be present and switch to it
#     # wait = WebDriverWait(driver, 10)
#     # close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal__header__close.js-modal-close')))
#     # close_button.click()
#     # Close the window
#     # driver.close()
#     if page == 1:
#         button = driver.find_element(By.CLASS_NAME, "modal-dialog__content__close")
#         button.click()
#
#         button = driver.find_element(By.CLASS_NAME, "lds__privacy-policy__btnClose")
#         button.click()
#
#     # Open the CSV file for writing
#     with open('products.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#
#         # Write the header row
#         writer.writerow(['Product SKU', 'Product Name', 'Product Brand', 'Product Price', 'Product Quantity', 'Size'])
#
#         for li in lis[count:]:
#             count += 1
#             div = li.find_element(By.TAG_NAME, 'div')
#             field = div.get_attribute('data-track-products-array')
#             # size = li.find_element(By.CLASS_NAME, "product-name__item--package-size")
#             size = SeleniumUtils.safe_find_element_text(li, By.CLASS_NAME, "product-name__item--package-size")
#             # Parse the JSON-encoded string
#             products = json.loads(field)
#             print(f"{page}:{count}")
#             # Print the product information
#             for product in products:
#                 print(f"{product['productSKU']}, {product['productName']}, {product['productBrand']}, "
#                       f"{product['productPrice']}, {product['productQuantity']}, {size}]\n")
#                 # for field in product:
#                 # print(f"{field} = {product[field]}")
#             # Write each product to the CSV file
#             for product in products:
#                 writer.writerow(
#                     [product['productSKU'], product['productName'], product['productBrand'], product['productPrice'],
#                      product['productQuantity'], size])
#
#         # FIND MORE BUTTON AND WAIT
#         wait = WebDriverWait(driver, 3)
#         # button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='LOAD 48 MORE RESULTS']")))
#         button = driver.find_element(By.CLASS_NAME, "primary-button--load-more-button")
#         # actions = Actions(driver)
#
#         # click the button
#         button.click()
#
#         listings = None
#
# with open('products2.html', 'w', newline='') as file:
#     file.write(driver.page_source)
