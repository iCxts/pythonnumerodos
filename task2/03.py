#Write function get_country_name(phone_number).
#phone_number should be in the format of '+XXOOOOOOOOOO' where +XX is the country code and other ten O characters is the number itself. This function should return string values:

def get_country_name(phone_number) -> str:
    if not isinstance(phone_number, str):
        raise TypeError('input must be a string')
    if len(phone_number) != 13:
        raise ValueError('invalid length')
    if not phone_number[0] == '+':
        raise LookupError('missing + prefix')


    country_code = phone_number[:3]
    number = phone_number[3:]

    if not (country_code[1:].isdigit() and number.isdigit()):
        raise ValueError('country code and phone number must be number')

    if country_code == '+34':
        return 'Spain'
    elif country_code == '+66':
        return 'Thailand'
    else:
        raise LookupError('unsupported country code')

    
    
