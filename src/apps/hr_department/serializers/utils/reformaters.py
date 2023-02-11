import base64
import re
from io import BytesIO
from uuid import uuid4

from PIL import Image
from django.core.files.base import ContentFile

from apps.hr_department.serializers.utils.fields import date_fields, iter_fields
from apps.hr_department.serializers.utils.token_refactor import jwt_token_refactor


def get_file_extension(file_name, decoded_data):
    image = Image.open(BytesIO(decoded_data))
    file_extension = image.format.lower()
    return f'{file_name}.{file_extension}'


def convert_base64_to_pillow_image(data):
    for field in data:
        if 'photo' in field:
            if data[field]:
                try:
                    data[field] = data[field].split(',')[1]
                    decoded_data = base64.b64decode(data[field].encode('utf-8'))
                    file_name = str(uuid4())[:12]
                    full_file_name = get_file_extension(file_name, decoded_data)
                    data[field] = ContentFile(decoded_data, name=full_file_name)
                except Exception as e:
                    data[field] = None


def reformat_date_fields(data):
    for field in date_fields:
        if field in data:
            if not data[field]:
                return
            # check format of date fields and reformat if needed
            if 'T' in data[field]:
                data[field] = data[field].split('T')[0]
            data[field] = data[field].replace('.', '-')


def reformat_documents(data, re_pattern, field_name):
    if field_name in data:
        if not data[field_name]:
            return
        # check format of document fields and reformat if needed
        # if not None
        if not data[field_name]:
            return
        if re.fullmatch(re_pattern, data[field_name]):
            data[field_name] = data[field_name].replace(' ', '')
            data[field_name] = data[field_name].replace('-', '')


def reformat_passport_number(data):
    reformat_documents(data, r'\d{4}\s\d{6}', 'passport_series_and_number')


def reformat_snils_number(data):
    reformat_documents(data, r'\d{3}\s\d{3}\s\d{3}\s\d{2}', 'snils_number')


def reformat_passport_division_code(data):
    reformat_documents(data, r'\d{3}\s\d{3}', 'passport_division_code')


def reformat_frontend_fields(data):
    reformat_date_fields(data)
    reformat_passport_number(data)
    reformat_snils_number(data)
    reformat_passport_division_code(data)
    jwt_token_refactor(data)


def reformat_iter_frontend_fields(data: dict):
    clear_data = data

    for infos_field in iter_fields:
        for field in infos_field['frontend_fields']:
            if "0__" + field['frontend_name'] in data:
                clear_data[infos_field['backend_name']] = []

    count = {
        i['backend_name']: data.keys().__str__().count(i['frontend_fields'][0]['frontend_name'])
        for i in iter_fields
    }

    for infos_field in iter_fields:
        for field in infos_field['frontend_fields']:
            for i in range(count[infos_field['backend_name']]):
                if f"{i}__" + field['frontend_name'] in data:
                    if infos_field['backend_name'] in clear_data:
                        if len(clear_data[infos_field['backend_name']]) < i + 1:
                            clear_data[infos_field['backend_name']].append({})
                        clear_data[infos_field['backend_name']][i][field['backend_name']] = data[
                            f"{i}__" + field['frontend_name']
                        ]
                    else:
                        clear_data[infos_field['backend_name']] = [
                            {field['backend_name']: data[f"{i}__" + field['frontend_name']]}
                        ]

    for infos_field in iter_fields:
        for field in infos_field['frontend_fields']:
            if "0__" + field['frontend_name'] in data:
                pass  # TODO: удалять лишние поля
