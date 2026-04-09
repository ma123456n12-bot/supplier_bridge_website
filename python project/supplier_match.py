print("=== Supplier Match System ===")

product = input("Enter required product: ")

if product.lower() == "electronics":
    print("Suggested Supplier Country: China")
elif product.lower() == "clothes":
    print("Suggested Supplier Country: Turkey")
elif product.lower() == "rice":
    print("Suggested Supplier Country: Pakistan")
else:
    print("No supplier found for this product.")