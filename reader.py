import json


def get_pet_list():
    with open('pets.json', 'r') as pets_file:
        pets_list = json.load(pets_file)
    return pets_list


def get_available_pets(tier):
    all_pets = get_pet_list()
    available_pets = []
    for pet in all_pets:
        if pet["tier"] == tier:
            available_pets.append(pet)

    return available_pets


def get_pet_list_names(pets_list):
    pet_name_list = []
    for pet in pets_list:
        pet_name_list.append(pet["name"])
    return pet_name_list
