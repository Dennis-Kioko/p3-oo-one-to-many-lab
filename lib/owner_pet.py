class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        Pet.all_pets.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_owned = []

    def pets(self):
        return self.pets_owned

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet unavailable")
        pet.owner = self
        self.pets_owned.append(pet)
    
    def get_sorted_pets(self):
        return sorted(self.pets_owned, key=lambda x: x.name)

# Testing the code
owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Whiskers", "cat", owner)
pet3 = Pet("Rex", "dog")

for pet in owner.get_sorted_pets():
    print(pet.name, "-", pet.pet_type)

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")

    assert pet1 in Pet.all_pets
