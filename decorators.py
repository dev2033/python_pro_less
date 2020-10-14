"""Декораторы в Python"""

# def null_decorator(func):
# 	"""Декорируемая функция"""
# 	return func

# @null_decorator
# def greet():
# 	"""Функция прогоняется через декоратор"""
# 	return 'Hello!'


"""Декораторы могут изменять поведения функции"""

# def uppercase(func):
# 	def wrapper():
# 		original_result = func()
# 		modified_result = original_result.upper()
# 		return modified_result
# 	return wrapper

# @uppercase
# def greet():
# 	return 'hello!'


"""Применение многочисленных декораторов к функции"""

# def strong(func):
# 	def wrapper():
# 		return '<strong>' + func() + '</strong>'
# 	return wrapper

# def paragraf(func):
# 	def wrapper():
# 		return '<p>' + func() + '</p>'
# 	return wrapper

# @strong
# @paragraf
# def greet():
# 	return 'Какой-то текст ...'

# print(greet())


"""
Декорирование функций, принимающих аргументы
(*args, **kwargs)
"""

# def proxy(func):
# 	def wrapper(*args, **kwargs):
# 		return func(*args, **kwargs)
# 	return wrapper

# def trace(func):
# 	def wrapper(*args, **kwargs):
# 		print(f'ТРАССИРОВКА: вызвана {func.__name__}()' f'с {args}, {kwargs}')

# 		original_result = func(*args, **kwargs)

# 		print(f'ТРАССИРОВКА: {func.__name__}()' f'вернула {original_result!r}')
# 		return original_result
# 	return wrapper

# @trace
# def say(name, line):
# 	return f'{name}: {line}'

# print(say('Джеин', 'Привет'))


"""Отлаживаемые дектораторы"""

import functools


def uppercase(func):
	@functools.wraps(func)
	def wrapper():
		return func().upper()
	return wrapper

@uppercase
def greet():
	"""Какие-то пояснения(docstring)"""
	return 'Hello'

print(greet())


