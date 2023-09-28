def two_number_division(x,y):
    for _ in range(1,101):
        if _ % x==0 and _ % y==0:
          print(_)

x=int(input(' enter x value'))
y=int(input(' enter y value'))

two_number_division(x,y)