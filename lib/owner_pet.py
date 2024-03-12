class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):

        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet".format(self.PET_TYPES))
        self.pet_type = pet_type
        self.name = name
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)