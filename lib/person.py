class Person:
    MIN_NAME_LENGTH = 1
    MAX_NAME_LENGTH = 25
    APPROVED_JOBS = ["Engineer", "Doctor", "Teacher", "Sales", "ITC"]

    def __init__(self, name="", job=""):
        self._name = ""
        self._job = ""
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and Person.MIN_NAME_LENGTH < len(value) <= Person.MAX_NAME_LENGTH:
            print(f"Setting name to {value}.")
            self._name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value


# Example usage:
