class Formula1Driver:
    # счетчик количества гонщиков
    drivers_count = 0

    def __init__(self, name, team):
        self.name = name
        self.team = team
        Formula1Driver.drivers_count += 1

    def get_info(self):
        return f"Имя: {self.name}, Команды: {self.team}"

    @staticmethod
    def count_drivers():  # статический метод для получения количества гонщиков
        return f"Всего гонщиков было : {Formula1Driver.drivers_count}"

    def create_driver_exempliar(self, driver_string):
        name, team = driver_string.split(",")  # разбиваем строки на части
        return self(name, team)  # Создаем экземпляр класса и возвращаем его


driver1 = Formula1Driver("Макс Ферстапен", "Red Bull Racing")
driver2 = Formula1Driver("Льюис Хэмильтон", "Mercedes")
driver3 = Formula1Driver("Фернандо Алонсо", "Aston Martin")
driver4 = Formula1Driver("Шарль Леклер", "Ferrari")

drivers = [driver1, driver2, driver3, driver4]

for index, driver in enumerate(drivers, start=1):
    print(f"Информация о гонщике {index}: ", driver.get_info())

print("Количество гонщиков участвующих в бахрейне : ", Formula1Driver.count_drivers())
