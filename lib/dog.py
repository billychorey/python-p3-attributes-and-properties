class Dog:
    MIN_NAME_LENGTH = 1
    MAX_NAME_LENGTH = 25
    APPROVED_BREEDS = ["Pug", "Beagle", "Labrador", "Bulldog"]

    def __init__(self, name="", breed=""):
        self._name = ""
        self._breed = ""
        self._set_name(name)
        self._set_breed(breed)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._set_name(value)

    def _set_name(self, value):
        if isinstance(value, str) and Dog.MIN_NAME_LENGTH < len(value) <= Dog.MAX_NAME_LENGTH:
            print(f"Setting name to {value}.")
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._set_breed(value)

    def _set_breed(self, value):
        if value not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
