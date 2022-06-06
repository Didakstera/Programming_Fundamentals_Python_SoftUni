number_of_orders = int(input())
total_price = 0
for orders in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 > price_per_capsule or 100 < price_per_capsule:
        continue
    elif 31 < days or 1 > days:
        continue
    elif capsules_per_day > 2000 or capsules_per_day < 1:
        continue
    else:
        coffee_price = price_per_capsule * capsules_per_day * days
        print(f"The price for the coffee is: ${coffee_price:.2f}")
        total_price += coffee_price
print(f"Total: ${total_price:.2f}")
