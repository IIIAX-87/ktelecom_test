import re


from equipment.models import EquipmentType, Equipment

mask_for_validate = {
    "N": "[0-9]",
    "A": "[A-Z]",
    "a": "[a-z]",
    "X": "[A-Z0-9]",
    "Z": "[-_@]"
}


def return_validate(serial_number, type_answer, i=0, mask=''):
    if type_answer == "error_len":
        return "Длинна серийного номера не соответсвует длинне макси серийного номера",
    if type_answer == "matched":
        return "Серийный номер соответствует маске серийного номера"
    else:
        return 'Символ № {} должен быть {}'.format(i+1, mask)


def validate_serial_number(serial_number, mask_serial_number, i=0):
    if len(serial_number) != len(mask_serial_number):
        return return_validate(serial_number, "error_len")
    for char in serial_number:
        mask = mask_for_validate[mask_serial_number[i]]
        matches = re.match(mask, char)
        if matches:
            i = i + 1
        else:
            return return_validate(serial_number, 'error_position', i, mask)
    return return_validate(serial_number, "matched")


def create_equipment(request):
    mask_serial_number = EquipmentType.objects.filter(id=request['equipment_type']).first()
    validate = validate_serial_number(serial_number=request['serial_number'],
                                      mask_serial_number=mask_serial_number.mask)
    if validate == "Серийный номер соответствует маске серийного номера":
        new_equipment = Equipment.objects.get_or_create(serial_number=request['serial_number'],
                                                        defaults={'serial_number': request['serial_number'],
                                                                  'equipment_type': mask_serial_number,
                                                                  'description': request['description']})
        if new_equipment[1]:
            return 'Оборудование с серийным номером {} успешно создано'.format(request['serial_number'])
        else:
            return 'Оборудование с серийным номером {} уже существует, объект не создан'.format(request['serial_number'])
    else:
        return validate


def create_equipments(requests, equipments=None):
    if equipments is None:
        equipments = []
    for request in requests:
        equipments.append(create_equipment(request))
    return equipments


def update_equipment(request):
    mask_serial_number = EquipmentType.objects.filter(id=request.data['equipment_type']).first()
    validate = validate_serial_number(serial_number=request.data['serial_number'],
                                      mask_serial_number=mask_serial_number.mask)
    if validate == "Серийный номер соответствует маске серийного номера":
        equipment = Equipment.objects.filter(pk=request.parser_context['kwargs']['pk']).first()
        equipment.serial_number = request.data['serial_number']
        equipment.equipment_type = mask_serial_number
        equipment.description = request.data['description']
        equipment.save()
        return 'Оборудование с серийным номером {} успешно обновлено'.format(request.data['serial_number'])
    else:
        return validate
