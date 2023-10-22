class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запускаем отрисовку с помощью ручки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запускаем отрисовку с помощью карандаша {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запускаем отрисовку с помощью маркера {self.title}")


pen1 = Pen("шариковой")
pencil1 = Pencil("простого")
handle1 = Handle("перманентного")

pen1.draw()
pencil1.draw()
handle1.draw()