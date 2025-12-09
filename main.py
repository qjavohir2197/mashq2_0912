#1-misol
tub_sonlar = tuple(
    num for num in range(2, 30+1)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
)

print(tub_sonlar)

#2-misol
my_tuple = (-3, -2, -1, 0, 1, 2, 3)

musbat_sonlar = tuple(x for x in my_tuple if x > 0)
print(musbat_sonlar)

#3-misol
my_tuple = tuple((x, x**2) for x in range(1, 15+1))

print(my_tuple)

#4-misol
matn = ['python', 'tuple', 'set', 'loop']

new = ()

for i in matn:
    new += (i[-1],)

print(new)

#5-misol
roy = tuple(x for x in range(1, 15+1) if x % 2 != 0)
print(roy)
