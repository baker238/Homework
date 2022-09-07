def discounted(price,discount,max_discout = 20):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return print(price_with_discount)

price_discounted = discounted(price,discount)
print(price_discounted)