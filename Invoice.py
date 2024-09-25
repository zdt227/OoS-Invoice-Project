#Class declaration
class Invoice:
    def __init__(self, vendor, brand, description, category, product_code, price):
        self.description = description
        self.category = category
        self.product_code = product_code
        self.brand = brand
        self.vendor = vendor
        self.price = price
    def setDescription(self, description):
        self.description = description
    def setCategory(self, category):
        self.category = category 
    def setProductCode(self, product_code):
        self.product_code = product_code
    def setBrand(self, brand):
        self.brand = brand
    def setVendor(self, vendor):
        self.vendor = vendor
    def setPrice(self, price):
        self.price = price