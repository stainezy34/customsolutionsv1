def save_product_descriptions(filename, product_descriptions):
    with open(filename, 'w') as file:
        for description in product_descriptions:
            file.write(description + '\n')

# Call the input function
input_set_number()

# Save the product descriptions to a file
filename = 'product_descriptions.txt'
save_product_descriptions(filename, product_descriptions)
