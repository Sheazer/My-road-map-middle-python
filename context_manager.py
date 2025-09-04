
"""
| Сценарий                                  | try/finally       | with/context manager            |
| ----------------------------------------- | ----------------- | ------------------------------- |
| Автоматическое открытие/закрытие ресурсов | ❌ Нужно руками    | ✅ Делает сам                    |
| Поддержка возврата объекта из блока       | ❌ Нет             | ✅ Можно через `__enter__`       |
| Обработка исключений                      | ❌ Нужно руками    | ✅ Можно прямо в `__exit__`      |
| Читаемость                                | ❌ Более громоздко | ✅ Лаконично, легко поддерживать |
"""

from contextlib import contextmanager


class contextmanager1(object):
    def __enter__(self):
        print("pre print")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("post print")
    
with contextmanager1() as cm:
    print("inside with block")

    
@contextmanager
def contextmanager2():
    print("pre print")
    yield
    print("post print")

with contextmanager2():
    print("inside with block2")

import time 

class Timer():

    def __enter__(self):
        self.time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Время выполнения блока: {time.time() - self.time} секунд")


with Timer():
    sum1 = 0
    for i in range(10000000):
        sum1 += i
    print(sum1)


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        print(f"Время выполнения блока: {time.time() - start:.4f} секунд")

# Используем
with timer():
    total = sum(range(10000000))
    print(total)