# task3_130121
"""
Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium
for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, group, name, price):
        self.group = group
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0

    def change_amount(self, amount):
        if self.amount + amount < 0:
            raise Exception (f'Не хватает {amount - self.amount}')
        self.amount += amount


class ProductStore:
    def __init__(self, price_premium=1.3):
        self.price_premium = price_premium
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount):
        name = product.name
        if name not in self.products.keys():
            self.products[name] = product
        self.products[name].change_amount(amount)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            if identifier not in self.products.keys():
                raise Exception(f'Товара нет на складе')
            else:
                self.products[identifier].discount = percent

    def sell_product(self, product_name, amount):
        if product_name not in self.products.keys():
            raise Exception(f'Товара нет на складе')
        for p in self.products:
            if p == product_name:
                self.products[p].change_amount(-amount)
                self.income += amount * self.products[p].price * ((100-self.products[p].discount)/100)

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products.values()


if __name__ == "__main__":
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)
    s.set_discount('Ramen', 5)
    s.sell_product('Ramen', 10)

