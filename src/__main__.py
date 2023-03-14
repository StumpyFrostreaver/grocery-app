from src.reader.metro_reader import MetroReader

reader = MetroReader()
products = reader.with_url('https://www.metro.ca/en/online-grocery/search?filter=coffee&freeText=true').parse()
print('\n\n\n\n\n')

for product in products:
    print(f'Name: {product.name} Brand: {product.brand}')

# # URL to be scraped
# url = "https://www.nofrills.ca/classic-roast-ground-coffee/p/21478183_EA"
#
# # Set up the Selenium WebDriver
# driver = webdriver.Chrome()
# driver.get(url)
#
# # Wait for the page to load
# time.sleep(5)
#
# # Find all the product listings on the page
# listings = driver.find_element(By.CLASS_NAME, 'site-content')
# divs = listings.find_elements(By.TAG_NAME, 'div')
# field = divs[0].get_attribute('data-track-products-array')
#
# # Parse the JSON-encoded string
# products = json.loads(field)
#
# # Print the product information
# for product in products:
#     print(f"Product SKU: {product['productSKU']}")
#     print(f"Product Name: {product['productName']}")
#     print(f"Product Brand: {product['productBrand']}")
#     print(f"Product Price: {product['productPrice']}")
#     print(f"Product Quantity: {product['productQuantity']}")
#
#
# # Open the CSV file for writing
# with open('products.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#
#     # Write the header row
#     writer.writerow(['Product SKU', 'Product Name', 'Product Brand', 'Product Price', 'Product Quantity'])
#
#     # Write each product to the CSV file
#     for product in products:
#         writer.writerow(
#             [product['productSKU'], product['productName'], product['productBrand'], product['productPrice'],
#              product['productQuantity']])
#
# print(field)
