#Помогаев Максим 2 вариант
class Machine:
    def __init__(self, productivity, price, average_price_part):
        self._productivity = productivity
        self._price = price
        self._average_price_part = average_price_part

    def __str__(self):
        return f'Станок: c производительностью {self._productivity} изделий в час, стоимость станка - {self._price}, средняя цена детали - {self._average_price_part}'
    
    def payback(self):
        return round(self._price / self._average_price_part)
    
    def payback_time(self):
        return round(self.payback() / self._productivity)
    
class Milling_machine(Machine):
    def __init__(self, productivity, price, average_price_part, detail):
        super().__init__(productivity, price, average_price_part)
        self._detail = detail
    
    def __str__(self):
        return super().__str__() + f' , форма деталей: {self._detail}'
    
    def treatment(self):
        if self._detail == "square":
            return self.payback() / 2
        elif self._detail == "circle":
            return self.payback() / 3
        else:
            return self.payback()

class CHPU_machine(Machine):
    def __init__(self, productivity, price, average_price_part, computer):
        super().__init__(productivity, price, average_price_part)
        self._computer = computer

    def __str__(self):
        return super().__str__() + f' , процессор компьютера: {self._computer}'
    
    def treatment(self):
        if self._computer == "new generation":
            return self.payback() / 10
        else:
            return self.payback() / 5
        
machine = Machine(5, 1000653, 100)
milling_machine = Milling_machine(10, 1000000054, 100, "square")
chpu_machine = CHPU_machine(15, 1000000000024424, 300, "new generation")
print(milling_machine.treatment())
print(machine.payback())
print(chpu_machine.treatment())
    

