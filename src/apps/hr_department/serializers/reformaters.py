from apps.hr_department.serializers.token_refactor import jwt_token_refactor


def reformat_date_fields(data):
    for field in date_fields:
        if field in data:
            data[field] = data[field].split('T')[0]
            data[field] = data[field].replace('.', '-')


def reformat_passport_number(data):
    if 'passport_series_and_number' in data:
        passport_number = data['passport_series_and_number'].replace(' ', '')
        data['passport_series_and_number'] = ''.join(passport_number)


def reformat_snils_number(data):
    if 'snils_number' in data:
        snils_number = data['snils_number'].replace(' ', '')
        snils_number = snils_number.replace('-', '')
        data['snils_number'] = ''.join(snils_number)


def reformat_passport_division_code(data):
    if 'passport_division_code' in data:
        passport_division_code = data['passport_division_code'].replace('-', '')
        data['passport_division_code'] = ''.join(passport_division_code)


def reformat_fields(data):
    reformat_date_fields(data)
    reformat_passport_number(data)
    reformat_snils_number(data)
    reformat_passport_division_code(data)
    jwt_token_refactor(data)