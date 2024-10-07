class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def __str__(self):
        return f'Наименование: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __eq__(self, other):
        return h1.numbers_of_floors == h2.numbers_of_floors

    def __lt__(self, other):
        return h1.numbers_of_floors < h2.numbers_of_floors


    def __le__(self,other):
        return h1.numbers_of_floors <= h2.numbers_of_floors


    def __gt__(self, other):
        return h1.numbers_of_floors > h2.numbers_of_floors


    def __ne__(self,other):
        return h1.numbers_of_floors != h2.numbers_of_floors


    def __ge__(self, other):
        return h1.numbers_of_floors <= h2.numbers_of_floors

    def __add__(self, value):
        self.numbers_of_floors = self.numbers_of_floors + value
        return h1


    def __iadd__(self, value):
        self.numbers_of_floors += value
        return h1


    def __radd__(self, value):
        self.numbers_of_floors = value + self.numbers_of_floors
        return h2



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print("равны ли:", h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print("равны ли после Эль+10:", h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print('Эль больше Акации:', h1 > h2) # __gt__
print('Эль больше или равен Акации:', h1 >= h2) # __ge__
print('Эль меньше Акации:', h1 < h2) # __lt__
print('Эль меньше или равен Акации:', h1 <= h2) # __le__
print('Эль не равен Акации:', h1 != h2) # __ne__
