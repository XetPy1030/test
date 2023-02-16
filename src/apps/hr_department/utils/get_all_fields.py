def get_all_fields_for_document(model):
    fields_list = []
    for field in model._meta.fields:
        # if type of django field == ImageField or FileField, then skip
        if type(field).__name__ == 'ImageField' or type(field).__name__ == 'FileField':
            continue
        if field.name == 'id':
            continue
        fields_list.append(field.name)
    return fields_list


def get_date_fields_for_document(model):
    date_fields_list = []
    fields_without_format = []
    other = []
    for field in model._meta.fields:
        # if type of django field == ImageField or FileField, then skip
        if type(field).__name__ == 'ImageField' or type(field).__name__ == 'FileField':
            continue
        if field.name == 'id':
            continue
        if type(field).__name__ == 'DateField':
            date_fields_list.append(field.name)
            continue
        elif field.name == "status":
            fields_without_format.append(field.name)
            continue
        else:
            other.append(field.name)
            continue
    return date_fields_list, fields_without_format, other
