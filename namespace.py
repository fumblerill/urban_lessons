def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() #Функция определяется и выполняется

test_function() #inner_function() определяется и выполняется
inner_function() # Программа не видит данную функцию