import threading
import time

# Общее количество врагов
enemies_count = 100


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global enemies_count  # Указываем, что enemies_count глобальна
        print(f"{self.name}, на нас напали!")

        days_passed = 0
        while enemies_count > 0:
            if enemies_count >= self.power:
                enemies_count -= self.power
            else:
                enemies_count = 0

            days_passed += 1
            time.sleep(1)  # Задержка на 1 секунду
            print(f"{self.name} сражается {days_passed} день(дня)..., осталось {enemies_count} воинов.")

        print(f"{self.name} одержал победу спустя {days_passed} дней(дня)!")

    # Создание объектов классов


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
