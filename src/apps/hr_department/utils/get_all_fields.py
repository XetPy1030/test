def get_all_fields_for_document(model):
    fields_list = []
    for field in model._meta.fields:
        if field.name == 'id':
            continue
        fields_list.append(field.name)
    return fields_list