def remove_word_from_sentence(x,y):
    list=[]
   
    for _ in x:
      list=x.split(' ')
    
    if y in list:
        list.remove(y)
    print(list)
          
x=input(' enter your sentence  ')
y=input(' enter your word  ')

remove_word_from_sentence(x,y)