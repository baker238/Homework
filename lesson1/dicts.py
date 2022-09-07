from math import prod
from pprint import pprint

product ={
    "name": "iphone 12",
    "stock": 24,
    "price": 65432.1
}
print(product)
product['memory'] = 256
pprint(product)
print(product["name"])#product.get["name", "что возвращать,если нет элемента"]
del product["name"]
#можно вкладывать списки 