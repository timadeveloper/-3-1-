a = int(input('Введите первую сторону:'))
b = int(input('Введите вторую сторону:'))
c = int(input('Введите третью сторону:'))
def area(a,b,c):
	p = (a+b+c)/2
	s = p*(p-a)*(p-b)*(p-c)
	sqr = s**(0.5)
	print('Площадь треугольника равна:', + sqr)

area(a,b,c)