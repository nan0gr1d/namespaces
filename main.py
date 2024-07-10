# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию def test_function
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        return   # из inner_function

    inner_function()  # здесь функция inner_function определена и работает

    return  # из test_function

test_function()   # работает

inner_function()  # не работает, в этом пространстве не определена

# Создайте другую функцию внутри функции inner_function, функция должна печатать значение
#  "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# Полученный код напишите в ответ к домашнему заданию