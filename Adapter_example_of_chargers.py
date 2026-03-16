from abc import ABC, abstractmethod


class ChargerInterface(ABC):
    @abstractmethod
    def charge(self):
        pass


class Phone:
    def charge_phone(self, charger: ChargerInterface):
        charger.charge()


class MicroUSBCharger:
    def micro_charge(self):
        print("Зарядка через MicroUSB.")


class TypeCCharger(ChargerInterface):
    def charge(self):
        print("Телефон заряжается через USB-C.")


class MicroUSBAdapter(ChargerInterface):

    def __init__(self, adaptee: MicroUSBCharger):
        self.adaptee = adaptee

    def charge(self):
        print("Используем адаптер MicroUSB → USB-C")
        self.adaptee.micro_charge()


phone = Phone()

print("Подключаем современную зарядку:")
type_c = TypeCCharger()
phone.charge_phone(type_c)

print("\nПодключаем старую зарядку через адаптер:")
old_charger = MicroUSBCharger()
adapter = MicroUSBAdapter(old_charger)

phone.charge_phone(adapter)