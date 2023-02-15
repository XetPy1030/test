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