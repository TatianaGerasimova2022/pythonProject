class Book:
    def __init__(self, name, autor, year):
        self.name = name
        self.autor = autor
        self.year = year

    def __str__(self):
        return 'Автор:' + self.autor + ',Название:' + self.name
