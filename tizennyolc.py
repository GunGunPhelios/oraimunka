product={
    "name" :"Sunglasses",
    "unitprice" :99.9,
    "taxable" : True,
    "instock": 10,
    "models": ["Green", "Black"]
}

print("Name: ", product["name"])
print("price: " , f"${product["unitprice"]:.2f}")
print("taxable ", product["taxable"])
print("instock:" , product["instock"])
print("Models: ")
for model in product["models"]:
    print("/t-" + model)