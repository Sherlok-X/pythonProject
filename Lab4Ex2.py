class Worker:
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._income = {"wage" : wage, "bonus" : bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surename}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

workers = [
    Position("Иван", "Иванович", "Программист", 2340, 1200),
    Position("Иван", "Кузьмич", "Танкист", 4340, 1720)
]

for worker in workers:
        print("Worker information")
        print("Full name:", worker.get_full_name())
        print("Workers positions:", worker.position)
        print("Total income:", worker.get_total_income())
        print()
