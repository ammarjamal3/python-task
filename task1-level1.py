def two_number_range(x,y):
    odd=[]
    even=[]
    for _ in range(x,y):
        if _ % 2==0:
          even.append(_)
        else: odd.append(_)
    print(f'odd number :{odd} \n even number : {even}')

x=int(input(' enter x value'))
y=int(input(' enter y value'))

two_number_range(x,y)
