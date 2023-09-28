names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha']
a,*b=names
print(a);print(b)

print('--------------')

a,*_,b=names
print(a);print(b)

print('--------------')

a,b,*_=names
print(a);print(b)