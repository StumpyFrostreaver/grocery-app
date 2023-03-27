from src.common.string_utils import StringUtils
from src.product.metro_product import MetroProduct
from src.reader.metro_reader import MetroReader
from src.product.voila_product import VoilaProduct
from src.reader.voila_reader import VoilaReader
from src.product.no_frills_product import NoFrillsProduct
from src.reader.no_frills_reader import NoFrillsReader

# reader = MetroReader()
# reader.with_url("https://www.metro.ca/en/online-grocery/search?filter=coffee&freeText=true")
# products = reader.parse()
#
# with open('../csv_files/mark/metro_coffee.csv', 'w', newline='') as file:
#     file.write(MetroProduct.as_csv_header()+'\n')
#
#     for product in products:
#         file.write(product.as_csv+'\n')


# reader = VoilaReader()
# reader.with_url("https://voila.ca/products/search?q=coffee")
# products = reader.parse()
#
#
# with open('../csv_files/mark/voila_coffee.csv', 'w', newline='') as file:
#     file.write(VoilaProduct.as_csv_header()+'\n')
#
#     for product in products:
#         file.write(product.as_csv+'\n')


reader = NoFrillsReader()
reader.with_url("https://www.nofrills.ca/search?search-bar=coffee%20food")
products = reader.parse()

with open('../csv_files/mark/nofrills_coffee.csv', 'w', newline='') as file:
    file.write(NoFrillsProduct.as_csv_header()+'\n')

    for product in products:
        file.write(product.as_csv+'\n')
