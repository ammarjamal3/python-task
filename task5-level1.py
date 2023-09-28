def sentence_size(x):
    list=[]
   
    for _ in x:
      list=x.split(' ')
    
    print(len(list))    

x=input(' enter your sentence  ')

sentence_size(x)