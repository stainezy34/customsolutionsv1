# customsolutionsv1
# main.py
from product_description_generator import generate_product_description

def input_set_number():
    sku = input("Enter the SET number or SKU: ")
    description = generate_product_description(sku)
    print(description)

# Test the input function
input_set_number()

# height_width_module_v1.py

from unit_configuration_module import calculate_total_units, determine_vehicle_type, get_unit_configuration
from product_description_manager import save_product_description
from height_roof_module import get_height

def generate_product_description(sku):
    height = get_height(sku)
    roof_type = get_roof_type(height)
    product_description = f'SET-{sku[len("SET-"):]}\n'
    product_description += f'Height: {height}mm\n\n'
    product_description += 'Product Description:\n'
    product_description += f'Unit Height: {height}mm ({roof_type})\n'

    width_unit = int(sku.split('-')[2])  # Extract the width unit from SKU
    total_install = int(sku.split('-')[3])  # Extract the total install width from SKU

    width_options = [429, 474, 500, 529, 600, 629]
    unit_configuration = get_unit_configuration(total_install, width_options)

    if unit_configuration:
        product_description += 'Unit Configuration:\n'
        for i, unit_width in enumerate(unit_configuration):
            product_description += f'{i+1}\N{COMBINING ENCLOSING KEYCAP} {unit_width}mm Standard Systainer\n'
    else:
        product_description += 'No exact unit configuration found.'

    vehicle_type = determine_vehicle_type(total_install)
    product_description += f'\nSuits {vehicle_type} (total install length: {total_install}mm)'

    total_widths = sum(unit_configuration) if unit_configuration else 0
    if total_widths > total_install:
        units_over = total_widths - total_install
        product_description += f"\nUnits Configured Over Total Length: {units_over}mm"
    elif total_widths < total_install:
        units_below = total_install - total_widths
        product_description += f"\nUnits Configured Below Total Length: {units_below}mm"

    difference = abs(total_widths - total_install)
    product_description += f"\nDifference between Total Units Widths and Install Length: {difference}mm"

    # Save the product description
    save_product_description(sku, product_description)

    return product_description


def input_set_number():
    while True:
        sku = input("Enter the SET number or SKU (or 'q' to quit): ")
        if sku.lower() == 'q':
            break
        description = generate_product_description(sku)
        print(description)


# Call the input function
input_set_number()

# height_roof_module.py
def get_roof_type(height):
    if height <= 1350:
        return 'H1 Standard Roof'
    elif 1351 <= height <= 1650:
        return 'H2 Medium Roof'
    elif 1651 <= height <= 2400:
        return 'H3 High Roof'

# product_description_generator.py

from unit_configuration_module import calculate_total_units, determine_vehicle_type, get_unit_configuration
from height_width_module_v1 import get_height, get_roof_type
from product_description_manager import save_product_description, input_set_number


def generate_product_description(sku, width_options):
    height = get_height(sku)
    roof_type = get_roof_type(height)
    product_description = f'SET-{sku[len("SET-"):]}\n'
    product_description += f'Height: {height}mm\n\n'
    product_description += 'Product Description:\n'
    product_description += f'Unit Height: {height}mm ({roof_type})\n'

    width_unit = int(sku.split('-')[2])  # Extract the width unit from SKU
    total_install = int(sku.split('-')[3])  # Extract the total install width from SKU

    unit_configuration = get_unit_configuration(total_install, width_options)

    if unit_configuration:
        product_description += 'Unit Configuration:\n'
        for i, unit_width in enumerate(unit_configuration):
            product_description += f'{i + 1} {unit_width}mm Standard Systainer\n'
    else:
        product_description += 'No exact unit configuration found.'

    vehicle_type = determine_vehicle_type(total_install)
    product_description += f'Suits {vehicle_type} (total install length: {total_install}mm)'

    total_widths = sum(unit_configuration) if unit_configuration else 0
    if total_widths > total_install:
        units_over = total_widths - total_install
        product_description += f'\nUnits Configured Over Total Length: {units_over}mm'
    elif total_widths < total_install:
        units_below = total_install - total_widths
        product_description += f'\nUnits Configured Below Total Length: {units_below}mm'

    difference = abs(total_widths - total_install)
    product_description += f'\nDifference between Total Units Widths and Install Length: {difference}mm'

    return product_description

# product_description_manager.py

from unit_configuration_module import calculate_total_units, determine_vehicle_type, get_unit_configuration
from height_width_module_v1 import get_height, get_roof_type
from product_description_manager import save_product_description, input_set_number

def save_product_descriptions(filename, product_descriptions):
    with open(filename, 'w') as file:
        for description in product_descriptions:
            file.write(description + '\n')

# Call the input function
input_set_number()

# Save the product descriptions to a file
filename = 'product_descriptions.txt'
save_product_descriptions(filename, product_descriptions)


# unit_configurations_module.py

def calculate_total_units(total_install, width_unit):
    if width_unit == 429:
        return total_install // width_unit
    else:
        return None

def determine_vehicle_type(total_install):
    if total_install <= 2300:
        return 'SWB (small wheelbase)'
    elif 2301 <= total_install <= 2900:
        return 'MWB (medium wheelbase)'
    else:
        return 'LWB (long wheelbase)'

def get_unit_configuration(total_install, width_options):
    # Code for getting the unit configuration based on total_install and width_options
    # ...

    return unit_configuration


# product_descriptions.txt
product_descriptions.txt
