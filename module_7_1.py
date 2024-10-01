
from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    def __init__(self, name: str, weight: float, category: str, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        __file_name = open(self.__file_name, 'r')  #r - read, w - write, a - append
        f = __file_name.read()
        __file_name.close()
        print(f'{f}')

    def add(self, *products):
        for i in products:
            s = (str(i))
            file_name = open(self.__file_name, 'r')
            file = file_name.read()
            file_name.close()
            if s in file:
               pprint(f'Продукт {s} уже есть в магазине')
            else:
                file_name = open(self.__file_name, 'a')
                file_name.write(f'\n {s}')
                file_name.close()


s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

