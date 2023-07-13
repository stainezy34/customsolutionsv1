from product_description_generator import generate_product_description

def input_set_number():
    sku = input("Enter the SET number or SKU: ")
    description = generate_product_description(sku)
    print(description)

# Test the input function
input_set_number()
