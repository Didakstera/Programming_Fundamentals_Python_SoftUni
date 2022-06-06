budget = float(input())
kg_flour_price = float(input())
eggs_collected = 0
loaves_made = 0
pack_eggs_price = kg_flour_price * 0.75
liter_milk = kg_flour_price * 0.25 + kg_flour_price
milk_for_one = liter_milk / 4
loaf_price = milk_for_one + pack_eggs_price + kg_flour_price
while budget > loaf_price:
    budget -= loaf_price
    loaves_made += 1
    eggs_collected += 3
    if loaves_made % 3 == 0:
        eggs_collected -= loaves_made - 2
print(f"You made {loaves_made} loaves of Easter bread! Now you have {eggs_collected} eggs and {budget:.2f}BGN left.")
