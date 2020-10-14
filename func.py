"""Функции в Python"""

def get_speak_func(text, volume) -> None:
  """Функции внутри функции. Как можно заметить, 
  внутрении функции не имеют параметра text, 
  они его 'захватывают' и 'запоминают'"""
    def whisper:
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


class Adder:
    """Класс, определяющий вызываемый объект"""
    def __init__(self, n) -> None:
        self.n = n

    def __call__(self, x):
        return self.n + x


# lambda-функции
"""
Так пишуться лямбда функции, вначале мы присваеваем 
переменной функцию, затем вызываем функцию и даем ей значения
"""
# add = lambda x, y: x + y
# add(5, 3)
# >> 8
"""
Та же функция add может быть определенная при помощи
ключевого слова def, она будет немного многословней
"""
def add(x: int, y: int):
  """После x и y стоить :int - это тайпхинтинги"""
  return(x + y)

print(add(32, 2))
