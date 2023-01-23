import base64
from io import BytesIO
from uuid import uuid4

from PIL import Image
from django.core.files.base import ContentFile

from apps.hr_department.serializers.fields import date_fields
from apps.hr_department.serializers.token_refactor import jwt_token_refactor


def get_file_extension(file_name, decoded_data):
    image = Image.open(BytesIO(decoded_data))
    file_extension = image.format.lower()
    return f'{file_name}.{file_extension}'


def convert_base64_to_pillow_image(data):
    for field in data:
        if 'photo' in field:
            if data[field]:
                decoded_data = base64.b64decode(data[field])
                file_name = str(uuid4())[:12]
                full_file_name = get_file_extension(file_name, decoded_data)
                data[field] = ContentFile(decoded_data, name=full_file_name)


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


def reformat_frontend_fields(data):
    reformat_date_fields(data)
    reformat_passport_number(data)
    reformat_snils_number(data)
    reformat_passport_division_code(data)
    convert_base64_to_pillow_image(data)
    jwt_token_refactor(data)
