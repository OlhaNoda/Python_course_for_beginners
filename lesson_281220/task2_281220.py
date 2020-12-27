# task2_281220
'''
Task 2
Computes and returns the total price of stock.
'''
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = {}
total = 0
for key, value in stock.items():
    total_price[key] = stock[key] * prices[key]
    total = total + stock[key] * prices[key]
print(f'total_price: {total_price} \ntotal: {total}')

