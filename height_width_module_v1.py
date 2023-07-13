def get_height(sku):
    height_code = sku.split('-')[1]  # Extract the height code from SKU
    if height_code.isdigit() and 700 <= int(height_code) <= 2400:
        height = int(height_code)
        return height
    else:
        raise ValueError('Invalid height code')

def get_roof_type(height):
    if height <= 1350:
        return 'H1 Standard Roof'
    elif 1351 <= height <= 1650:
        return 'H2 Medium Roof'
    elif 1651 <= height <= 2400:
        return 'H3 High Roof'
    else:
        return 'Not available'
