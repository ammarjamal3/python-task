def multiplication(x,y):
    for x in range(x,y):
        for y in range(y):
          print(f'{x} X {y} = {x*y}')

x=int(input(' enter x value'))
y=int(input(' enter y value'))

multiplication(x,y)