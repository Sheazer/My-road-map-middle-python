
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
