#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# la funcion retornara el valor 5  

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#la funcion retornara el 5 ademas mostrarra error por que hay una funcion que no esta definida 

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# retorna los dos numeros que se le indica (5 y 10)


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#retorna el numero 5  y ademas imprime el numero 10


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# en primera instancia imprimira el numero 5, luego imprimira funcion number_of_great_lakes, que corresponde al valor de x


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# mostrara como resultado 8

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#entregara las letras que estan en el puesto 2 y 5 de la palabra concatenar


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#imprimira el valor 100 y  luego 10 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#impimira 14,7,14,14


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#imprime 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#imprime 500, 300,500,300,500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#imprime 500,300,300,300


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500, 300, 500,300,500


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 1,2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1,bar,nose que mas sigue profe :(