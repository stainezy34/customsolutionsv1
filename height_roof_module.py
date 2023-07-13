def get_roof_type(height):
    if height <= 1350:
        return 'H1 Standard Roof'
    elif 1351 <= height <= 1650:
        return 'H2 Medium Roof'
    elif 1651 <= height <= 2400:
        return 'H3 High Roof'

