class Cat:
    def __init__(self, name, gender, age, status):
        self.name = name
        self.gender = gender
        self.age = age
        self.status = status

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_status(self):
        return self.status

    def save(self):
        with open('cats', 'a') as x:
            x.write(f'{self.get_name(), self.get_gender(), self.get_age(), self.get_status()}'+'\n')

