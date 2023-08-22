class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def name(self):
        return self._name

    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    def breed(self):
        return self._breed

    def breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")


fido = Dog("Fido", "Mastiff")

fido.name = ""
