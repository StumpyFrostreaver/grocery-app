from src.product.metro_product import MetroProduct
from src.reader.metro_reader import MetroReader
from src.product.voila_product import VoilaProduct
from src.reader.voila_reader import VoilaReader

# reader = MetroReader()
# reader.with_url("https://www.metro.ca/en/online-grocery/search?filter=coffee&freeText=true")
# products = reader.parse()
#
# with open('../csv_files/mark/metro_coffee.csv', 'w', newline='') as file:
#     file.write(MetroProduct.as_csv_header()+'\n')
#
#     for product in products:
#         file.write(product.as_csv+'\n')


reader = VoilaReader()
reader.with_url("https://voila.ca/products/search?q=coffee")
products = reader.parse()


with open('../csv_files/mark/voila_coffee.csv', 'w', newline='') as file:
    file.write(VoilaProduct.as_csv_header()+'\n')

    for product in products:
        file.write(product.as_csv+'\n')
