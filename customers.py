
# ISM2411 Lab 11 - Dictionaries and Lookup
# Reflection Questions
#
# 1. I would use .get() when I am not sure if a key is in the
# dictionary because it wont cause an error if its missing.
# I would use brackets when I know the key is there.
# My rule is to use .get() if the key might be missing.
#
# 2. This reminds me of pivot tables in Excel because they
# both group data and calculate totals. Python can be better
# for large datasets because it can process a lot of data
# automatically without having to do everything manually.


# Exercise 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print("Exercise 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2 - Update and Add

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3 - Safe Lookup

print("\nExercise 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email is not in the dictionary")


# Exercise 4 - Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys
# instead of both the keys and values.

for key in customer:
    print(key)


# Exercise 5 - Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)

print("Tier:", tier)
print("Discount:", f"{discount * 100}%")
print("Final Price:", f"${final_price:.2f}")


# Exercise 6 - List of Dicts

print("\nExercise 6")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{name} - {tier} - Discount: ${discount_amount:.2f}")


# Exercise 7 - Nested Catalog

print("\nExercise 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# Exercise 8 - Sales by Region

print("\nExercise 8")

transactions = [
    {"region": "North", "amount": 100},
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 150},
    {"region": "North", "amount": 50},
    {"region": "South", "amount": 300}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
