def can_be_divided(x,y):
    list=[]
   
    for q in range(x,101):
      if q % y ==0:
         print(q)
      
x=int(input(' enter x value  '))
y=int(input(' enter x value  '))

can_be_divided(x,y)