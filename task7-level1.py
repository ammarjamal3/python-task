def number_of_duplicate(x,y):
    list=[]
   
    for _ in x:
      list=x.split(' ')
      
    print(list.count(y))
          
x=input(' enter your sentence  ')
y=input(' enter your word  ')

number_of_duplicate(x,y)