from height_width_module_v1 import get_height, get_roof_type
from unit_configuration_module import calculate_total_units, determine_vehicle_type, get_unit_configuration

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

    return product_description
