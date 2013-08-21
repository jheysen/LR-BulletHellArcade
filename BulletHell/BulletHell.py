print('Hello World')
print('asdf')
print('mensaje')

def fib(n):
    a,b = 0,1
    while a<n:
        print a,
        a,b = b,a+b

num = int(raw_input('Introduzca un número: '))
fib(num)
print('')