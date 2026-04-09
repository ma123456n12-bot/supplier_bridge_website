print("=== Client Inquiry Form ===")

client_name = input("Enter client name: ")
company_name = input("Enter company name: ")
product_needed = input("Enter product needed: ")
supplier_country = input("Enter supplier country: ")

file = open("inquiries.txt", "a")

file.write("Client Name: " + client_name + "")
file.write("Company Name: " + company_name + "")
file.write("Product Needed: " + product_needed + "")
file.write("Supplier Country: " + supplier_country + "")
file.write("--------------------------")

file.close()

print("Inquiry saved successfully.")