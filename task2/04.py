#Write function get_country_name(phone_number).
#phone_number should be in the format of '+XXOOOOOOOOOO' where +XX is the country code and other ten O characters is the number itself. This function should return string values:


def get_country_name(phone_number) -> str:
    assert isinstance(phone_number, str), 'TypeError: input must be a string'
    assert len(phone_number) >= 3, 'ValueError: invalid length'

    assert phone_number[0] == '+', 'LookupError: missing + prefix'

    country_code = phone_number[:3]
    number = phone_number[3:]

    assert len(country_code) == 3 and country_code[1:].isdigit(), \
        'ValueError: country code must be 2 digits'

    assert len(number) == 10, 'ValueError: number must be 10 digits'
    assert len(phone_number) == 13, 'ValueError, total length must be 13'

    if country_code == '+34':
        return 'Spain'
    elif country_code == '+66':
        return 'Thailand'
    return 'unknown'    
    
