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
