from unit_configuration_module import calculate_total_units, determine_vehicle_type, get_unit_configuration
from height_width_module_v1 import get_height, get_roof_type
from height_roof_module import get_roof_type

def generate_product_description(sku, width_options):
    height = get_height(sku)
    roof_type = get_roof_type(height)
    product_description = 'SET-{}\n'.format(sku[len("SET-"):])
    product_description += 'Height: {}mm\n\n'.format(height)
    product_description += 'Product Description:\n'
    product_description += 'Unit Height: {}mm ({})\n'.format(height, roof_type)

    width_unit = int(sku.split('-')[2])  # Extract the width unit from SKU
    total_install = int(sku.split('-')[3])  # Extract the total install width from SKU

    unit_configuration = get_unit_configuration(total_install, width_options)

    if unit_configuration:
        product_description += 'Unit Configuration:\n'
        for i, unit_width in enumerate(unit_configuration):
            product_description += '{} {}mm Standard Systainer\n'.format(i + 1, unit_width)
    else:
        product_description += 'No exact unit configuration found.'

    vehicle_type = determine_vehicle_type(total_install)
    product_description += 'Suits {} (total install length: {}mm)'.format(vehicle_type, total_install)

    total_widths = sum(unit_configuration) if unit_configuration else 0
    if total_widths > total_install:
        units_over = total_widths - total_install
        product_description += '\nUnits Configured Over Total Length: {}mm'.format(units_over)
    elif total_widths < total_install:
        units_below = total_install - total_widths
        product_description += '\nUnits Configured Below Total Length: {}mm'.format(units_below)

    difference = abs(total_widths - total_install)
    product_description += '\nDifference between Total Units Widths and Install Length: {}mm'.format(difference)

    return product_description
