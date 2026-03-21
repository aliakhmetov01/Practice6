from functools import reduce

a = [1, 2, 3]
b = [4, 5, 6]

zip_ab = zip(a, b)
product_ab = [x * y for x, y in zip_ab]
dot_product_ab = reduce(lambda x, y: x + y, product_ab)
print(dot_product_ab)