from django.apps import apps


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


def get_model_by_name(app_name, model_name):
    try:
        model = apps.get_model(app_name, model_name)
        return model
    except LookupError:
        return None


def get_date_fields_for_document(model):
    date_fields_list = []
    fields_without_format = []
    nested_fields = []
    other = []
    # get ManyToMany fields
    # print(model._meta.__dict__)
    for field in model._meta.fields:
        # if type of django field == ImageField or FileField, then skip
        if type(field).__name__ == 'ImageField' or type(field).__name__ == 'FileField':
            continue
        if field.name == 'id':
            continue
        if type(field).__name__ == 'DateField':
            date_fields_list.append(field.name)
            continue
        elif field.name == "status" or field.name == "gender":
            fields_without_format.append(field.name)
            continue
        else:
            other.append(field.name)
            continue
    for field in model._meta.local_many_to_many:
        nested_fields.append(field)
    return date_fields_list, fields_without_format, nested_fields, other
